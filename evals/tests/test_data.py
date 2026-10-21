"""Integrity tests for the TRIZ data files and the lookup script.

Run from the repo root: python -m unittest discover -s evals/tests
"""

import csv
import io
import json
import re
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "triz"
DATA = SKILL / "data"
sys.path.insert(0, str(SKILL / "scripts"))

import matrix_lookup  # noqa: E402


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


class ParametersTest(unittest.TestCase):
    def test_39_parameters_with_ids_in_order(self):
        params = load("parameters.json")["parameters"]
        self.assertEqual([p["id"] for p in params], list(range(1, 40)))

    def test_fields(self):
        for p in load("parameters.json")["parameters"]:
            self.assertTrue(p["name"].strip(), p)
            self.assertTrue(p["definition"].strip(), p)
            self.assertIsInstance(p["aliases"], list)
            self.assertTrue(all(isinstance(a, str) and a for a in p["aliases"]), p)

    def test_names_unique(self):
        names = [p["name"].lower() for p in load("parameters.json")["parameters"]]
        self.assertEqual(len(names), len(set(names)))


class PrinciplesTest(unittest.TestCase):
    def test_40_principles_with_ids_in_order(self):
        principles = load("principles.json")["principles"]
        self.assertEqual([p["id"] for p in principles], list(range(1, 41)))

    def test_fields(self):
        for p in load("principles.json")["principles"]:
            self.assertTrue(p["name"].strip(), p)
            self.assertIsInstance(p["aliases"], list)
            self.assertGreaterEqual(len(p["subprinciples"]), 1, p["id"])
            self.assertEqual(set(p["examples"]),
                             {"engineering", "software", "business", "everyday"}, p["id"])
            self.assertTrue(all(v.strip() for v in p["examples"].values()), p["id"])

    def test_known_names(self):
        by_id = {p["id"]: p["name"] for p in load("principles.json")["principles"]}
        self.assertEqual(by_id[1], "Segmentation")
        self.assertEqual(by_id[10], "Preliminary action")
        self.assertEqual(by_id[35], "Parameter changes")
        self.assertEqual(by_id[40], "Composite materials")


class MatrixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(DATA / "contradiction-matrix.csv", encoding="utf-8", newline="") as f:
            cls.rows = list(csv.reader(f))
        cls.matrix = matrix_lookup.load_matrix()

    def test_shape_and_headers(self):
        self.assertEqual(len(self.rows), 40)
        self.assertEqual(self.rows[0][1:], [str(i) for i in range(1, 40)])
        self.assertEqual([r[0] for r in self.rows[1:]], [str(i) for i in range(1, 40)])
        for row in self.rows:
            self.assertEqual(len(row), 40, row[0])

    def test_cell_format(self):
        for row in self.rows[1:]:
            for cell in row[1:]:
                self.assertRegex(cell, r"^(\d+(;\d+){0,3})?$")

    def test_ids_in_range_and_unique_per_cell(self):
        for key, ids in self.matrix.items():
            self.assertTrue(all(1 <= i <= 40 for i in ids), key)
            self.assertEqual(len(ids), len(set(ids)), key)
            self.assertLessEqual(len(ids), 4, key)

    def test_diagonal_empty(self):
        for i in range(1, 40):
            self.assertEqual(self.matrix[(i, i)], [], i)

    def test_filled_cell_count(self):
        # Both sources read on 2026-10-21 have 1,248 filled cells.
        self.assertEqual(sum(1 for ids in self.matrix.values() if ids), 1248)

    def test_known_cells(self):
        known = {
            (1, 9): [2, 8, 15, 38],
            (1, 3): [15, 8, 29, 34],
            (9, 12): [35, 15, 18, 34],
            (19, 9): [8, 35],
            (23, 38): [35, 10, 18],
            (25, 27): [10, 30, 4],
            (39, 38): [5, 12, 35, 26],
            (9, 39): [],
            (2, 1): [],
        }
        for key, ids in known.items():
            self.assertEqual(self.matrix[key], ids, key)


class StatusTest(unittest.TestCase):
    def test_status_file(self):
        data = load("matrix-status.json")
        meta = data["_meta"]
        self.assertIn(meta["default_status"], meta["statuses"])
        self.assertIsInstance(meta["book_verified"], bool)
        for key, status in data["cells"].items():
            self.assertRegex(key, r"^\d+-\d+$")
            i, w = map(int, key.split("-"))
            self.assertTrue(1 <= i <= 39 and 1 <= w <= 39, key)
            self.assertIn(status, meta["statuses"], key)

    def test_no_verified_cell_before_book_check(self):
        data = load("matrix-status.json")
        if not data["_meta"]["book_verified"]:
            self.assertNotEqual(data["_meta"]["default_status"], "verified")
            self.assertNotIn("verified", data["cells"].values())

    def test_disputed_cells_are_logged(self):
        data = load("matrix-status.json")
        log = (DATA / "matrix-discrepancies.md").read_text(encoding="utf-8")
        for key, status in data["cells"].items():
            if status == "disputed":
                self.assertRegex(log, rf"\|\s*{re.escape(key)}\s*\|", key)


class SeparationTest(unittest.TestCase):
    def test_four_types(self):
        seps = load("separation.json")["separations"]
        self.assertEqual([s["type"] for s in seps], ["time", "space", "condition", "system level"])
        for s in seps:
            self.assertTrue(s["question"].endswith("?"))
            self.assertTrue(s["principle_ids"])
            self.assertTrue(all(1 <= i <= 40 for i in s["principle_ids"]), s["type"])


class LookupScriptTest(unittest.TestCase):
    def run_cli(self, *args):
        out = io.StringIO()
        with redirect_stdout(out):
            code = matrix_lookup.main(list(args))
        return code, out.getvalue()

    def test_single_lookup_json(self):
        code, out = self.run_cli("--improve", "25", "--worsen", "27", "--json")
        self.assertEqual(code, 0)
        result = json.loads(out)
        self.assertEqual([p["id"] for p in result["principles"]], [10, 30, 4])
        self.assertEqual(result["principles"][0]["name"], "Preliminary action")
        self.assertEqual(result["status"], "cross-checked")

    def test_lookup_by_name_and_alias(self):
        code, out = self.run_cli("--improve", "speed", "--worsen", "shape", "--json")
        self.assertEqual(code, 0)
        self.assertEqual([p["id"] for p in json.loads(out)["principles"]], [35, 15, 18, 34])
        code, out = self.run_cli("--improve", "throughput", "--worsen", "27", "--json")
        self.assertEqual(json.loads(out)["improving"], 39)

    def test_ambiguous_name_fails(self):
        with redirect_stdout(io.StringIO()), self.assertRaises(ValueError):
            matrix_lookup.resolve_parameter("weight", matrix_lookup.load_parameters())

    def test_merge_ranks_by_frequency(self):
        code, out = self.run_cli("--merge", "9:12", "39:27", "--json")
        self.assertEqual(code, 0)
        ranked = json.loads(out)["ranked"]
        self.assertEqual(ranked[0], {"id": 35, "name": "Parameter changes", "count": 2})
        self.assertEqual([p["id"] for p in ranked[1:]], [15, 18, 34, 1, 10, 38])

    def test_diagonal_points_to_separation(self):
        code, out = self.run_cli("--improve", "9", "--worsen", "9")
        self.assertEqual(code, 0)
        self.assertIn("physical contradiction", out)

    def test_principle(self):
        code, out = self.run_cli("--principle", "10", "--json")
        self.assertEqual(json.loads(out)["name"], "Preliminary action")

    def test_bad_id(self):
        import contextlib
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code, _ = self.run_cli("--improve", "40", "--worsen", "1")
        self.assertEqual(code, 2)
        self.assertIn("no parameter 40", err.getvalue())


class SkillFrontmatterTest(unittest.TestCase):
    def test_name_matches_folder_and_description(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        self.assertIsNotNone(match, "SKILL.md needs YAML frontmatter")
        front = match.group(1)
        name = re.search(r"^name:\s*(\S+)\s*$", front, re.M)
        self.assertIsNotNone(name)
        self.assertEqual(name.group(1), SKILL.name)
        desc = re.search(r"^description:\s*(.+(?:\n[ \t]+.+)*)", front, re.M)
        self.assertIsNotNone(desc)
        self.assertLessEqual(len(" ".join(desc.group(1).split())), 1024)


if __name__ == "__main__":
    unittest.main()
