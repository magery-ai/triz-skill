"""Checks for the online contradiction matrix built by tools/build_site.py.

Run from the repo root: python -m unittest discover -s evals/tests
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import build_site  # noqa: E402


class SiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = build_site.build(Path(cls.tmp.name) / "_site")
        cls.data = json.loads((cls.out / "data.json").read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_data_counts(self):
        self.assertEqual(len(self.data["parameters"]), 39)
        self.assertEqual(len(self.data["principles"]), 40)
        self.assertEqual(len(self.data["matrix"]), 1248)

    def test_disputed_cells_carry_the_other_value(self):
        self.assertEqual(len(self.data["disputed"]), 29)
        self.assertEqual(self.data["disputed"]["9-1"], [8, 28, 13, 38])
        self.assertEqual(self.data["disputed"]["35-37"], [])

    def test_principle_pages_and_sitemap(self):
        sitemap = (self.out / "sitemap.xml").read_text(encoding="utf-8")
        for p in self.data["principles"]:
            self.assertTrue((self.out / p["page"]).exists(), p["page"])
            self.assertIn(p["page"], sitemap)

    def test_index_lists_principles(self):
        index = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("<!--PRINCIPLES-->", index)
        self.assertIn("principles/40-composite-materials.html", index)


if __name__ == "__main__":
    unittest.main()
