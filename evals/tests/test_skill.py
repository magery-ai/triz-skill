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
                and not line.startswith(("| Term", "| Parameter"))]
        self.assertGreater(len(rows), 50)
        for row in rows:
            cell = row.split("|")[2].strip()
            refs = re.findall(r"(\d+) ([^,]+)", cell)
            self.assertTrue(refs, row)
            for pid, name in refs:
                self.assertEqual(names.get(int(pid)), name.strip(), row)

    def matrix(self):
        cells = {}
        rows = [line.split(",") for line in read("data/contradiction-matrix.csv").splitlines()]
        for row in rows[1:]:
            for col, cell in zip(rows[0][1:], row[1:]):
                cells[(int(row[0]), int(col))] = cell
        return cells

    def test_worked_merges_use_filled_cells(self):
        cells = self.matrix()
        merges = re.findall(r"`--merge ([\d: ]+)`", read("guides/domain-mapping.md"))
        self.assertTrue(merges)
        for pair in re.findall(r"(\d+):(\d+)", " ".join(merges)):
            a, b = map(int, pair)
            self.assertTrue(cells[(a, b)] or cells[(b, a)], f"{a}:{b} is empty both ways")

    def test_populated_and_empty_lists_match_matrix(self):
        cells = self.matrix()
        section = read("guides/domain-mapping.md").split("## Cost, speed and quality", 1)[1]
        section = section.split("\n## ", 1)[0]
        for line in section.split("\n- ")[1:]:
            pairs = [tuple(map(int, p)) for p in re.findall(r"(\d+):(\d+)", line)]
            for a, b in pairs:
                filled = bool(cells[(a, b)]) and bool(cells[(b, a)])
                empty = not cells[(a, b)] and not cells[(b, a)]
                if line.startswith("**Empty"):
                    self.assertTrue(empty, f"{a}:{b} listed as empty")
                else:
                    self.assertTrue(filled, f"{a}:{b} listed as populated")


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


class PlanFieldsTest(unittest.TestCase):
    FIELDS = ["Resources", "Watch for", "Done when"]

    def test_short_template_has_required_fields(self):
        text = read("templates/plan-short.md")
        for field in self.FIELDS:
            self.assertIn(f"**{field}:**", text)

    def test_full_template_has_required_fields(self):
        text = read("templates/plan-full.md")
        section = text.split("## 9.", 1)[1].split("\n## ", 1)[0]
        for field in self.FIELDS:
            self.assertIn(f"**{field}**", section)

    def test_examples_fill_required_fields(self):
        for path in sorted((SKILL / "examples").glob("*.md")):
            if path.name == "TEMPLATE.md":
                continue
            plan = path.read_text(encoding="utf-8").split("## Short plan", 1)[1]
            for field in self.FIELDS:
                match = re.search(rf"^\*\*{field}:\*\* (.+)$", plan, re.M)
                self.assertIsNotNone(match, f"{path.name}: {field}")
            for field in ["Watch for", "Done when"]:
                line = re.search(rf"^\*\*{field}:\*\* (.+)$", plan, re.M).group(1)
                self.assertRegex(line, r"\d", f"{path.name}: {field} has no number")


class QuestionBudgetTest(unittest.TestCase):
    def test_skill_states_budget(self):
        text = read("SKILL.md")
        self.assertIn("## Question budget", text)
        self.assertIn("5-8 user turns", text)

    def test_stage_files_cap_questions(self):
        self.assertIn("at most 2 clarifying questions", read("workflow/1-intake.md"))
        self.assertIn("at most 2", read("workflow/5-socratic.md"))


if __name__ == "__main__":
    unittest.main()
