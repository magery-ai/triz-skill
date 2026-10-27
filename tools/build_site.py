"""Build the static website: an online contradiction matrix plus one page per
inventive principle, all generated from skills/triz/data.

Usage: python tools/build_site.py [--out _site]

The site is deployed to GitHub Pages by .github/workflows/pages.yml. Open
_site/index.html through a local server (python -m http.server -d _site),
because the page loads data.json with fetch().
"""

import argparse
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DATA = ROOT / "skills" / "triz" / "data"
BASE_URL = "https://magery-ai.github.io/triz-skill/"
REPO_URL = "https://github.com/magery-ai/triz-skill"

sys.path.insert(0, str(ROOT / "skills" / "triz" / "scripts"))

import matrix_lookup  # noqa: E402

DOMAINS = [
    ("software", "Software"),
    ("business", "Business"),
    ("engineering", "Engineering"),
    ("everyday", "Everyday life"),
]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def principle_path(principle):
    return f"principles/{principle['id']}-{slug(principle['name'])}.html"


def disputed_values():
    """Return {"i-w": [principle ids]} for the 1973 table's value of each disputed cell."""
    text = (DATA / "matrix-discrepancies.md").read_text(encoding="utf-8")
    section = text.split("### Content differences", 1)[1].split("###", 1)[0]
    values = {}
    for row in re.finditer(r"^\| (\d+-\d+) \|[^|]*\|[^|]*\| ([^|]*) \|", section, re.M):
        values[row.group(1)] = [int(x) for x in re.findall(r"\d+", row.group(2))]
    return values


def site_data():
    parameters = matrix_lookup.load_parameters(DATA)
    principles = matrix_lookup.load_principles(DATA)
    matrix = matrix_lookup.load_matrix(DATA)
    _, status, _ = matrix_lookup.load_status(DATA)
    other = disputed_values()
    return {
        "parameters": [
            {k: p[k] for k in ("id", "name", "definition", "aliases")}
            for p in parameters.values()
        ],
        "principles": [
            {
                "id": p["id"],
                "name": p["name"],
                "subprinciples": p["subprinciples"],
                "examples": p["examples"],
                "page": principle_path(p),
            }
            for p in principles.values()
        ],
        "matrix": {f"{i}-{w}": ids for (i, w), ids in matrix.items() if ids},
        "disputed": {
            f"{i}-{w}": other.get(f"{i}-{w}", [])
            for (i, w), s in status.items()
            if s == "disputed"
        },
    }


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}social-preview.png">
<link rel="icon" href="../logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<header class="top"><a class="brand" href="../"><picture><source media="(prefers-color-scheme: dark)" srcset="../logo-dark.svg"><img src="../logo.svg" alt="" width="28" height="28"></picture>TRIZ contradiction matrix</a>
<a class="gh" href="{repo}">GitHub</a></header>
<main class="narrow">
<p class="crumb"><a href="../#principles">40 inventive principles</a> / #{id}</p>
<h1><span class="num">#{id}</span> {name}</h1>
{aliases}
<h2>What it says</h2>
<ul>{subprinciples}</ul>
<h2>Examples</h2>
<dl class="examples">{examples}</dl>
<h2>Where the matrix suggests it</h2>
<p>The classic contradiction matrix suggests {name} in {count} of its 1,248 filled cells. Most often for these conflicts:</p>
<ul>{cells}</ul>
{cta}
<nav class="pager">{prev}{next}</nav>
</main>
</body>
</html>
"""

CTA = """<aside class="cta">
<h2>Let your agent do this</h2>
<p>The <a href="{repo}">TRIZ skill</a> teaches Claude and other AI agents to find
the contradiction in your problem, look it up in this matrix and turn the
principles into a plan with a metric and a date. Free and MIT licensed.</p>
<pre><code>/plugin marketplace add magery-ai/triz-skill
/plugin install triz@triz-skill</code></pre>
</aside>"""


def principle_page(p, data, by_id):
    params = {q["id"]: q["name"] for q in data["parameters"]}
    hits = [
        key for key, ids in data["matrix"].items() if p["id"] in ids
    ]
    # Cells where the principle comes first are its strongest recommendations.
    hits.sort(key=lambda k: (data["matrix"][k].index(p["id"]), [int(x) for x in k.split("-")]))
    cells = "".join(
        f'<li><a href="../?improve={i}&amp;worsen={w}">Improving {html.escape(params[int(i)])}'
        f" worsens {html.escape(params[int(w)])}</a></li>"
        for i, w in (k.split("-") for k in hits[:8])
    )
    examples = "".join(
        f"<dt>{label}</dt><dd>{html.escape(p['examples'][key])}</dd>"
        for key, label in DOMAINS
        if key in p["examples"]
    )
    prev_p, next_p = by_id.get(p["id"] - 1), by_id.get(p["id"] + 1)

    def nav(q, rel, arrow):
        if not q:
            return "<span></span>"
        text = f'#{q["id"]} {html.escape(q["name"])}'
        text = f"{arrow} {text}" if rel == "prev" else f"{text} {arrow}"
        return f'<a rel="{rel}" href="../{q["page"]}">{text}</a>'

    name = html.escape(p["name"])
    first_example = p["examples"].get("software", "")
    return PAGE.format(
        title=f"TRIZ principle {p['id']}: {name}, with examples",
        description=html.escape(
            f"TRIZ inventive principle {p['id']}, {p['name']}: what it says, examples from "
            f"software, business and engineering, and where the contradiction matrix suggests it. "
            f"{first_example}"
        ),
        url=BASE_URL + p["page"],
        base=BASE_URL,
        repo=REPO_URL,
        id=p["id"],
        name=name,
        aliases=(
            f'<p class="aliases">Also called: {html.escape(", ".join(p["aliases"]))}</p>'
            if p.get("aliases") else ""
        ),
        subprinciples="".join(f"<li>{html.escape(s)}</li>" for s in p["subprinciples"]),
        examples=examples,
        count=len(hits),
        cells=cells,
        cta=CTA.format(repo=REPO_URL),
        prev=nav(prev_p, "prev", "&larr;"),
        next=nav(next_p, "next", "&rarr;"),
    )


def build(out_dir):
    out = Path(out_dir)
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(SITE, out)
    shutil.copy(ROOT / "assets" / "logo-light.svg", out / "logo.svg")
    shutil.copy(ROOT / "assets" / "logo-dark.svg", out / "logo-dark.svg")
    shutil.copy(ROOT / "assets" / "social-preview.png", out / "social-preview.png")
    data = site_data()
    index = out / "index.html"
    items = "\n".join(
        f'<li value="{p["id"]}"><a href="{p["page"]}">{html.escape(p["name"])}</a></li>'
        for p in data["principles"]
    )
    index.write_text(index.read_text(encoding="utf-8").replace("<!--PRINCIPLES-->", items), encoding="utf-8")
    (out / "data.json").write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    by_id = {p["id"]: p for p in data["principles"]}
    (out / "principles").mkdir()
    for p in data["principles"]:
        (out / p["page"]).write_text(principle_page(p, data, by_id), encoding="utf-8")
    urls = [BASE_URL] + [BASE_URL + p["page"] for p in data["principles"]]
    (out / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
        + "</urlset>\n",
        encoding="utf-8",
    )
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n", encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default="_site")
    args = parser.parse_args()
    print(build(args.out))


if __name__ == "__main__":
    main()
