# Changelog

## 0.2.0 (unreleased)

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

## 0.1.0 (unreleased)

- Skill skeleton: `skills/triz/SKILL.md` with trigger description, core rules,
  stage map, modes (guided, fast, autonomous) and state block.
- Draft workflow files for the six stages plus autonomous mode.
- Short and full plan templates; example template.
