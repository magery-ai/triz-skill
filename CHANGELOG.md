# Changelog

## 0.3.0 (unreleased)

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
