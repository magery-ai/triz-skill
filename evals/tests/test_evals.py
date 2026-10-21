"""Checks for the eval cases and trigger set.

Run from the repo root: python -m unittest discover -s evals/tests
"""

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVALS = ROOT / "evals"
sys.path.insert(0, str(ROOT / "skills" / "triz" / "scripts"))

import matrix_lookup  # noqa: E402

REQUIRED = ["id", "domain", "mode", "prompt", "persona",
            "expected_contradictions", "checks"]
PAIR_RE = re.compile(
    r"- improving: (\d+) (.+)\n\s+worsening: (\d+) (.+)\n\s+principles: \[([\d, ]*)\]")


class CasesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = {p: p.read_text(encoding="utf-8")
                     for p in sorted((EVALS / "cases").glob("*.yaml"))}
        cls.matrix = matrix_lookup.load_matrix()
        cls.names = {i: p["name"] for i, p in matrix_lookup.load_parameters().items()}

    def test_count_and_modes(self):
        modes = [re.search(r"^mode: (\w+)", t, re.M).group(1) for t in self.cases.values()]
        self.assertGreaterEqual(modes.count("guided") + modes.count("fast"), 10)
        self.assertGreaterEqual(modes.count("autonomous"), 3)

    def test_required_keys_and_id(self):
        for path, text in self.cases.items():
            for key in REQUIRED:
                self.assertRegex(text, rf"(?m)^{key}:", f"{path.name} lacks {key}")
            self.assertEqual(re.search(r"^id: (\S+)", text, re.M).group(1), path.stem)

    def test_persona_only_for_human_modes(self):
        for path, text in self.cases.items():
            autonomous = "\nmode: autonomous" in text
            self.assertEqual("\npersona: none" in text, autonomous, path.name)

    def test_expected_cells_match_matrix(self):
        for path, text in self.cases.items():
            pairs = PAIR_RE.findall(text)
            self.assertTrue(pairs, path.name)
            for imp, imp_name, wor, wor_name, cell in pairs:
                imp, wor = int(imp), int(wor)
                self.assertEqual(self.names[imp], imp_name.strip(), path.name)
                self.assertEqual(self.names[wor], wor_name.strip(), path.name)
                expected = [int(x) for x in cell.split(",") if x.strip()]
                self.assertEqual(self.matrix[(imp, wor)], expected,
                                 f"{path.name}: cell {imp}x{wor}")


class TriggersTest(unittest.TestCase):
    def test_counts(self):
        text = (EVALS / "triggers.yaml").read_text(encoding="utf-8")
        should, should_not = text.split("should_not_trigger:")
        self.assertGreaterEqual(len(re.findall(r"(?m)^  - ", should)), 20)
        self.assertGreaterEqual(len(re.findall(r"(?m)^  - ", should_not)), 10)


if __name__ == "__main__":
    unittest.main()
