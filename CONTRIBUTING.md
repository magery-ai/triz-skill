# Contributing

Thanks for helping. The skill gets better from real problems, so examples and
eval cases are the most useful contributions.

## Ground rules

- English only.
- Write in your own words. Do not copy text from TRIZ books or paid sources;
  describing a fact (such as a matrix value) and citing the source is fine.
- Keep `skills/triz/SKILL.md` under 200 lines; put detail in the stage files.
- Run the tests before opening a pull request:
  `python -m unittest discover -s evals/tests`.

## Repository layout

```
skills/triz/
├── SKILL.md            # trigger, rules, stage map, modes, state block
├── workflow/           # one file per stage, plus autonomous.md
├── guides/             # domain-mapping.md: software, business, personal terms
├── templates/          # plan-short.md, plan-full.md
├── data/               # parameters, principles, matrix, separation, check status
├── scripts/            # matrix_lookup.py (standard library only)
└── examples/           # worked examples, plus TEMPLATE.md
.claude-plugin/         # marketplace.json for Claude Code
tools/build_zip.py      # builds the Claude.ai release zip
tools/build_site.py     # builds the online matrix from site/ and data/
site/                   # online matrix page, deployed by pages.yml
evals/
├── cases/              # 13 scenario cases (10 guided or fast, 3 autonomous)
├── triggers.yaml       # should / should-not trigger prompts
├── rubric.md           # how to grade a run
└── tests/              # data, script, structure and case tests, run in CI
```

Run the tests with `python -m unittest discover -s evals/tests`. See
[`evals/README.md`](evals/README.md) for trigger tests and scenario evals.

## Add a worked example

1. Copy `skills/triz/examples/TEMPLATE.md` to
   `skills/triz/examples/<domain>-<short-slug>.md`.
2. Keep each gate visible in the conversation, and cite the matrix cell you
   used. Check it with `python skills/triz/scripts/matrix_lookup.py`.
3. Remove anything private.

If you'd rather not open a pull request, use the
[Submit a worked example](https://github.com/magery-ai/triz-skill/issues/new?template=worked-example.yml)
issue form.

## Add an eval case

Copy any file in `evals/cases/`, rename it to `<domain>-<short-slug>.yaml`,
and fill in every key. The tests check that each `expected_contradictions`
entry names real parameters and the exact matrix cell, so run them after
editing. Add a case for each bug you find in real use. See
[`evals/README.md`](evals/README.md) for how cases are run and graded.

## Report a wrong matrix cell

Open a [Wrong matrix cell](https://github.com/magery-ai/triz-skill/issues/new?template=wrong-matrix-cell.yml)
issue with the parameter pair, the current value, the value in your source,
and the source itself. If it is confirmed, the fix updates
`contradiction-matrix.csv`, logs both values in `matrix-discrepancies.md`, and
sets the cell's status in `matrix-status.json`.

## Change the workflow

Open an issue first for anything beyond a wording fix, describing the problem
the change solves. Changes to a stage should come with an eval case that shows
the improvement.
