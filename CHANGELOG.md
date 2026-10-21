# Changelog

## 1.0.0 (2026-10-21)

First release.

- Claude Code plugin marketplace entry: `.claude-plugin/marketplace.json`, so
  `/plugin marketplace add magery-ai/triz-skill` works.
- Release zip for Claude.ai (`triz-skill-1.0.0.zip`, one `triz/` folder),
  built by `tools/build_zip.py` and attached to each GitHub Release by
  `.github/workflows/release.yml` when a `v*.*.*` tag is pushed.
- Matrix status: all 1,521 cells agree between triz40.com and a second copy
  except one logged typo-level difference (19x9). The cells have not been
  checked against Altshuller's *40 Principles* (Shulyak and Rodman, 1997);
  `matrix-status.json` says so, and the "Wrong matrix cell" issue form is the
  way to report a cell.
- `evals/tests/test_release.py`: marketplace paths and versions, zip layout.

## 0.4.0 (not released separately)

- `evals/cases/`: 13 scenario cases (4 engineering, 3 software, 2 business,
  1 personal, 3 autonomous), each with a prompt, a scripted persona, expected
  contradictions with their matrix cells, and checks.
- `evals/triggers.yaml` (20 should, 10 should not), `evals/rubric.md`, and
  `evals/README.md` on how to run and grade cases.
- `evals/tests/test_evals.py`: every expected cell in the cases must match the
  matrix.
- Worked examples: wind turbine blade, cache vs freshness, support speed vs
  quality.
- README example fixed to match the matrix (#10, #1 from cells 25x27 and
  39x27).
- Issue templates "Wrong matrix cell" and "Submit a worked example", a link to
  Discussions, and CONTRIBUTING.md.

## 0.3.0 (not released separately)

- Workflow: full instructions for all six stages and autonomous mode. Intake
  gets an IFR guide with examples and a resource checklist; contradiction gets
  cause chains, TC and PC forms, candidate format and checks; directions covers
  empty and reverse cells, merging and separation; actions get an action
  format, filter rules and a scoring table; plan delivery gets slug and file
  rules.
- `workflow/5-socratic.md`: question bank of 30 questions, 5 for each of the
  six types, with selection, stop and loop-back rules.
- `workflow/autonomous.md`: assumption log, contradiction ranking, critic pass
  (self-critique or critic agent), 2-loop cap and confidence rubric.
- `guides/domain-mapping.md`: software, business and personal terms mapped to
  the 39 parameters, with three worked mappings.
- SKILL.md example now uses the real matrix cells (#10, #1 from merging
  25:27 and 39:27).
- `evals/tests/test_skill.py`: frontmatter, length, file references, mapping
  names and question bank checks.

## 0.2.0 (not released separately)

- Data: `parameters.json` (39 parameters with definitions and aliases),
  `principles.json` (40 principles with sub-principles and examples for
  engineering, software, business and everyday life), `separation.json`.
- `contradiction-matrix.csv`: the classic 39x39 matrix from triz40.com,
  cross-checked against a second copy (1 typo-level difference, logged in
  `matrix-discrepancies.md`). Per-cell check status in `matrix-status.json`;
  not yet checked against the book.
- `scripts/matrix_lookup.py`: single and merged lookups, name and alias
  search, JSON output. Standard library only.
- `evals/tests/test_data.py` and a GitHub Actions workflow that runs it.

## 0.1.0 (not released separately)

- Skill skeleton: `skills/triz/SKILL.md` with trigger description, core rules,
  stage map, modes (guided, fast, autonomous) and state block.
- Draft workflow files for the six stages plus autonomous mode.
- Short and full plan templates; example template.
