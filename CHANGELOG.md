# Changelog

## Next

- A cell-by-cell check of the matrix against Altshuller's *40 Principles*
  (Shulyak and Rodman, 1997).

## 1.2.0 (2026-10-21)

- Autonomous mode gives the caller engineering depth: stage 1 breaks the
  target metric into its parts and looks for a bottleneck the obvious fix
  misses, and the returned message adds an execution section (measure first,
  every lever from no-risk to risky, a path-to-target table with its margin,
  verification before switching, deliverables). The 400-word cap is gone.
  In a blind re-run of the 3 autonomous cases (5 runs), the skill was
  preferred in 5 of 5, up from 1 of 3. Results in
  `evals/results/2026-10-21-autonomous.md`.
- Two worked examples from AI engineering, linked from the README: a model
  router that halves the inference bill without worse answers (fast mode),
  and OCR with field checks in place of an LLM for invoice extraction
  (guided mode).

## 1.1.0 (2026-10-21)

- First full with/without eval run (13 cases, blind grading): the skill
  passed 123 of 124 items against 92, and was preferred in 11 of 13 cases.
  Results in `evals/results/2026-10-21.md`, with a chart and summary in the
  README.
- Stage 4 now starts from the expert levers (the 2-4 quantities that drive A
  and B, with rough numbers), estimates how far each action moves the user's
  target, and does not lower the target without the user's consent. Found in
  the first with/without eval pilot, where the baseline beat the skill on a
  drone case by spotting hover efficiency.
- Autonomous mode returns an action-first message (confidence, executable
  short plan, rollback, high-impact assumptions, a one-line critic result,
  full-plan path) in about 400
  words, with the analysis kept in the full plan. Found in the same pilot,
  where the baseline's CI plan was easier for a coding agent to act on.
- `agents/AGENTS.md`: a compact rules-file version of the workflow for
  agents that can't load skills, reading the matrix from this repository.
  Linked from README and INSTALL.md, with a test that its links resolve.
- README rebuilt around a short first screen: logo, one-line promise, badges,
  a before/after image, install near the top with an "ask your agent" line,
  an example table with the full session collapsed, a stage diagram, a modes
  table and a FAQ. The matrix status note moved to Sources, the repository
  layout to CONTRIBUTING.md and the version roadmap here. New INSTALL.md with
  every install option.
- Domain mapping: software "serving cost" (cost per request, inference bill)
  now maps to 23 Loss of substance instead of 32 Ease of manufacture, which is
  empty against 27 Reliability in both directions. New rows for serving cost
  and model answer quality, a list of populated and empty cost/speed vs
  quality pairs, a neighbours table for empty cells, and a worked "cheaper
  inference vs reliable answers" mapping.
- Explicit empty-cell rule in stage 3: reverse cell, say it plainly,
  closest neighbour (confirmed in guided mode, stated in fast mode, an
  assumption in autonomous mode), then separation only. The question budget
  allows this one stage 3 question.
- Tests that worked merges and the populated/empty lists match the matrix.
- Required plan fields: every short and full plan, in every mode, now has
  **Resources** (what it uses, and anything new with its cost), **Watch for**
  (the top risk, a signal with a threshold, and what to do when it is
  crossed) and **Done when** (a metric tied to the IFR, a target and a date).
  `workflow/6-plan.md` defines what each must contain; the full plan's
  section 9 holds them as tables. The examples and README show all three.
- Question budget for guided mode: at most 2 clarifying questions in intake
  and 2 Socratic questions in validation, one at a time, aiming at a plan in
  about 5-8 user turns. The intake and contradiction checks merge into one
  turn when intake leaves nothing open, and the approval request shares a
  turn with the last Socratic answer. More questions only when the user asks
  or a loop-back needs it. Fast mode: at most 1 clarifying question and 2
  skippable risk questions. Autonomous mode is unchanged.
- Rubric: new "Question budget" and "Plan fields" items; the Socratic item
  now expects 2 questions instead of at least 3.
- Tests for the required fields in the templates and examples, and for the
  question budget in the stage files.

## 1.0.0 (2026-10-21)

First release.

- Claude Code plugin marketplace entry: `.claude-plugin/marketplace.json`, so
  `/plugin marketplace add magery-ai/triz-skill` works.
- Release zip for Claude.ai (`triz-skill-1.0.0.zip`, one `triz/` folder),
  built by `tools/build_zip.py` and attached to each GitHub Release by
  `.github/workflows/release.yml` when a `v*.*.*` tag is pushed.
- Matrix status: all 1,521 cells agree between triz40.com and a second copy
  except one logged typo-level difference (19x9). A third copy, the 1973
  table published by the G.S. Altshuller Foundation, agrees on the principles
  in 1,492 cells; 29 cells differ and are marked `disputed`, with both values
  in `matrix-discrepancies.md`. The cells have not been checked against
  Altshuller's *40 Principles* (Shulyak and Rodman, 1997), and the "Wrong
  matrix cell" issue form is the way to report a cell.
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
