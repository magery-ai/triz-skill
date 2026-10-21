"""Structure tests for SKILL.md, the workflow files and the guides.

Run from the repo root: python -m unittest discover -s evals/tests
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "triz"

PATH_RE = re.compile(r"`((?:workflow|guides|templates|data|scripts|examples)/[\w./-]+)`")


def read(rel):
    return (SKILL / rel).read_text(encoding="utf-8")


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError("SKILL.md has no frontmatter")
    fields, key = {}, None
    for line in match.group(1).splitlines():
        if re.match(r"^\w[\w-]*:", line):
            key, _, value = line.partition(":")
            fields[key] = value.strip()
        elif key:
            fields[key] += " " + line.strip()
    return fields


class SkillFileTest(unittest.TestCase):
    def test_frontmatter(self):
        fields = frontmatter(read("SKILL.md"))
        self.assertEqual(fields["name"], SKILL.name)
        self.assertTrue(re.fullmatch(r"[a-z0-9-]{1,64}", fields["name"]))
        self.assertTrue(0 < len(fields["description"]) <= 1024)
        self.assertNotIn("<", fields["description"])

    def test_short(self):
        self.assertLess(len(read("SKILL.md").splitlines()), 200)

    def test_stage_map_lists_every_workflow_file(self):
        text = read("SKILL.md")
        for f in sorted((SKILL / "workflow").glob("*.md")):
            self.assertIn(f"workflow/{f.name}", text)


class ReferencesTest(unittest.TestCase):
    def test_referenced_paths_exist(self):
        files = [SKILL / "SKILL.md", *SKILL.glob("workflow/*.md"), *SKILL.glob("guides/*.md")]
        for f in files:
            for ref in PATH_RE.findall(f.read_text(encoding="utf-8")):
                if "<" in ref or "*" in ref:
                    continue
                self.assertTrue((SKILL / ref).exists(), f"{f.name} points to missing {ref}")


class DomainMappingTest(unittest.TestCase):
    def test_parameter_refs_match_names(self):
        names = {p["id"]: p["name"] for p in
                 json.loads(read("data/parameters.json"))["parameters"]}
        rows = [line for line in read("guides/domain-mapping.md").splitlines()
                if line.startswith("|") and not line.startswith("|--")
                and not line.startswith("| Term")]
        self.assertGreater(len(rows), 50)
        for row in rows:
            cell = row.split("|")[2].strip()
            refs = re.findall(r"(\d+) ([^,]+)", cell)
            self.assertTrue(refs, row)
            for pid, name in refs:
                self.assertEqual(names.get(int(pid)), name.strip(), row)


class SocraticBankTest(unittest.TestCase):
    TYPES = ["Clarification", "Assumptions", "Evidence", "Viewpoints",
             "Consequences", "The question itself"]

    def test_six_types_five_questions_each(self):
        text = read("workflow/5-socratic.md")
        bank = text.split("## Question bank", 1)[1].split("\n## ", 1)[0]
        sections = re.split(r"^### ", bank, flags=re.M)[1:]
        self.assertEqual([s.splitlines()[0].strip() for s in sections], self.TYPES)
        for s in sections:
            questions = re.findall(r"^\d+\. ", s, re.M)
            self.assertEqual(len(questions), 5, s.splitlines()[0])


if __name__ == "__main__":
    unittest.main()
