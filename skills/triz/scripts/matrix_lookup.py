#!/usr/bin/env python3
"""Look up the classic TRIZ contradiction matrix.

Examples:
  matrix_lookup.py --improve 9 --worsen 12
  matrix_lookup.py --improve speed --worsen "loss of time"
  matrix_lookup.py --merge 9:12 9:14 25:27
  matrix_lookup.py --find throughput
  matrix_lookup.py --principle 35

Python standard library only. Reads the files in ../data next to this script.
"""

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_json(name, data_dir=DATA_DIR):
    with open(data_dir / name, encoding="utf-8") as f:
        return json.load(f)


def load_parameters(data_dir=DATA_DIR):
    return {p["id"]: p for p in load_json("parameters.json", data_dir)["parameters"]}


def load_principles(data_dir=DATA_DIR):
    return {p["id"]: p for p in load_json("principles.json", data_dir)["principles"]}


def load_matrix(data_dir=DATA_DIR):
    """Return {(improving, worsening): [principle ids]} for every cell."""
    matrix = {}
    with open(data_dir / "contradiction-matrix.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    columns = [int(c) for c in rows[0][1:]]
    for row in rows[1:]:
        improving = int(row[0])
        for worsening, cell in zip(columns, row[1:]):
            matrix[(improving, worsening)] = [int(x) for x in cell.split(";") if x]
    return matrix


def load_status(data_dir=DATA_DIR):
    """Return (default status, {(improving, worsening): status}, meta)."""
    data = load_json("matrix-status.json", data_dir)
    cells = {}
    for key, status in data["cells"].items():
        improving, worsening = key.split("-")
        cells[(int(improving), int(worsening))] = status
    return data["_meta"]["default_status"], cells, data["_meta"]


def resolve_parameter(value, parameters):
    """Turn an id or a name/alias into a parameter id."""
    value = str(value).strip()
    if value.isdigit():
        pid = int(value)
        if pid in parameters:
            return pid
        raise ValueError(f"no parameter {pid}; ids run 1-{len(parameters)}")
    matches = find_parameters(value, parameters)
    exact = [p for p in matches if value.lower() == p["name"].lower()
             or value.lower() in (a.lower() for a in p["aliases"])]
    if len(exact) == 1:
        return exact[0]["id"]
    if len(matches) == 1:
        return matches[0]["id"]
    if not matches:
        raise ValueError(f"no parameter matches {value!r}; try --find")
    names = ", ".join(f"{p['id']} {p['name']}" for p in matches)
    raise ValueError(f"{value!r} matches several parameters: {names}; use an id")


def find_parameters(term, parameters):
    term = term.lower()
    return [p for p in parameters.values()
            if term in p["name"].lower() or any(term in a.lower() for a in p["aliases"])]


def lookup(improving, worsening, matrix, principles, status):
    default, cells, _ = status
    ids = matrix[(improving, worsening)]
    return {
        "improving": improving,
        "worsening": worsening,
        "principles": [{"id": i, "name": principles[i]["name"]} for i in ids],
        "status": cells.get((improving, worsening), default),
    }


def merge(pairs, matrix, principles, status):
    """Look up several pairs and rank principles by how many cells name them.

    Ties keep the order of first appearance.
    """
    results = [lookup(i, w, matrix, principles, status) for i, w in pairs]
    counts = Counter()
    first_seen = {}
    for result in results:
        for p in result["principles"]:
            counts[p["id"]] += 1
            first_seen.setdefault(p["id"], len(first_seen))
    ranked = sorted(counts, key=lambda pid: (-counts[pid], first_seen[pid]))
    return {
        "cells": results,
        "ranked": [{"id": pid, "name": principles[pid]["name"], "count": counts[pid]}
                   for pid in ranked],
    }


def format_cell(result, parameters):
    imp, wor = result["improving"], result["worsening"]
    lines = [f"Improving {imp} {parameters[imp]['name']} / "
             f"worsening {wor} {parameters[wor]['name']}  [{result['status']}]"]
    if not result["principles"]:
        if imp == wor:
            lines.append("  Same parameter on both sides: this is a physical contradiction.")
            lines.append("  Use the separation principles in data/separation.json.")
        else:
            lines.append("  Empty cell: the matrix gives no principles for this pair.")
            lines.append("  Try the closest neighbouring parameters, or separation principles.")
    for p in result["principles"]:
        lines.append(f"  #{p['id']} {p['name']}")
    return "\n".join(lines)


def parse_pair(text):
    if ":" not in text:
        raise ValueError(f"pair {text!r} must look like IMPROVE:WORSEN, e.g. 9:12")
    left, right = text.split(":", 1)
    return left, right


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Look up principles in the classic TRIZ contradiction matrix.")
    parser.add_argument("--improve", help="improving parameter: id or name")
    parser.add_argument("--worsen", help="worsening parameter: id or name")
    parser.add_argument("--merge", nargs="+", metavar="IMPROVE:WORSEN",
                        help="several pairs; principles are ranked by frequency")
    parser.add_argument("--find", metavar="TERM", help="search parameters by name or alias")
    parser.add_argument("--principle", type=int, metavar="ID", help="show one principle")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args(argv)

    parameters = load_parameters()
    principles = load_principles()

    def emit(obj, text):
        print(json.dumps(obj, indent=2, ensure_ascii=False) if args.json else text)

    try:
        if args.find:
            found = find_parameters(args.find, parameters)
            emit(found, "\n".join(f"{p['id']:>2} {p['name']}" for p in found)
                 or f"No parameter matches {args.find!r}.")
            return 0
        if args.principle is not None:
            p = principles.get(args.principle)
            if p is None:
                raise ValueError(f"no principle {args.principle}; ids run 1-40")
            text = [f"#{p['id']} {p['name']}"] + [f"  - {s}" for s in p["subprinciples"]]
            text += [f"  {k}: {v}" for k, v in p["examples"].items()]
            emit(p, "\n".join(text))
            return 0

        matrix = load_matrix()
        status = load_status()
        if args.merge:
            pairs = []
            for item in args.merge:
                left, right = parse_pair(item)
                pairs.append((resolve_parameter(left, parameters),
                              resolve_parameter(right, parameters)))
            result = merge(pairs, matrix, principles, status)
            text = [format_cell(c, parameters) for c in result["cells"]]
            text.append("Ranked:")
            text += [f"  #{p['id']} {p['name']} (x{p['count']})" for p in result["ranked"]]
            emit(result, "\n".join(text))
            return 0
        if args.improve and args.worsen:
            result = lookup(resolve_parameter(args.improve, parameters),
                            resolve_parameter(args.worsen, parameters),
                            matrix, principles, status)
            emit(result, format_cell(result, parameters))
            return 0
        parser.error("give --improve and --worsen, --merge, --find or --principle")
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
