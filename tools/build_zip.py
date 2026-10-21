"""Build the release zip for uploading the skill to Claude.ai.

Usage: python tools/build_zip.py [--out dist]

The zip holds one top-level folder, triz/, with SKILL.md inside it, which is
the layout Claude.ai expects for an uploaded skill.
"""

import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "triz"
SKIP = {"__pycache__", ".DS_Store"}


def version():
    with open(ROOT / ".claude-plugin" / "marketplace.json", encoding="utf-8") as f:
        return json.load(f)["metadata"]["version"]


def skill_files():
    for path in sorted(SKILL.rglob("*")):
        if path.is_file() and not SKIP.intersection(path.parts) and path.suffix != ".pyc":
            yield path


def build(out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"triz-skill-{version()}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in skill_files():
            zf.write(path, Path("triz") / path.relative_to(SKILL))
    return target


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default=str(ROOT / "dist"), help="output folder")
    args = parser.parse_args(argv)
    print(build(args.out))


if __name__ == "__main__":
    main()
