"""Checks for the plugin marketplace entry and the release zip.

Run from the repo root: python -m unittest discover -s evals/tests
"""

import json
import re
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import build_zip  # noqa: E402


class MarketplaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(ROOT / ".claude-plugin" / "marketplace.json", encoding="utf-8") as f:
            cls.data = json.load(f)
        with open(ROOT / ".claude-plugin" / "plugin.json", encoding="utf-8") as f:
            cls.manifest = json.load(f)

    def test_skill_paths_exist(self):
        self.assertTrue((ROOT / "skills" / "triz" / "SKILL.md").exists())

    def test_plugin_manifest_matches_marketplace(self):
        entry = self.data["plugins"][0]
        self.assertTrue(entry["strict"])
        self.assertEqual(self.manifest["name"], entry["name"])
        self.assertEqual(self.manifest["version"], self.data["metadata"]["version"])
        # The plugin ships no subagents; portable/AGENTS.md is for other tools.
        self.assertEqual(self.manifest["agents"], [])

    def test_versions_agree_with_changelog(self):
        version = self.data["metadata"]["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertTrue(all(p["version"] == version for p in self.data["plugins"]))
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        top = re.search(r"^## (\d+\.\d+\.\d+)", changelog, re.M).group(1)
        self.assertEqual(top, version)


class ZipTest(unittest.TestCase):
    def test_layout(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = build_zip.build(tmp)
            self.assertEqual(target.name, f"triz-skill-{build_zip.version()}.zip")
            with zipfile.ZipFile(target) as zf:
                names = zf.namelist()
        self.assertIn("triz/SKILL.md", names)
        self.assertIn("triz/data/contradiction-matrix.csv", names)
        self.assertIn("triz/scripts/matrix_lookup.py", names)
        self.assertTrue(all(n.startswith("triz/") for n in names))
        self.assertFalse(any("__pycache__" in n for n in names))


if __name__ == "__main__":
    unittest.main()


class CompactRulesTest(unittest.TestCase):
    RAW = "https://raw.githubusercontent.com/magery-ai/triz-skill/main/"

    def test_raw_links_point_to_real_files(self):
        text = (ROOT / "portable" / "AGENTS.md").read_text(encoding="utf-8")
        links = re.findall(re.escape(self.RAW) + r"(\S+)", text)
        self.assertTrue(links)
        for rel in links:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_short(self):
        text = (ROOT / "portable" / "AGENTS.md").read_text(encoding="utf-8")
        self.assertLess(len(text.splitlines()), 120)
