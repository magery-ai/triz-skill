# Autonomous re-run, 2026-10-21

> Superseded by the [multi-run results](2026-10-21-multirun.md) (3 runs per arm).

The [full run](2026-10-21.md) lost both autonomous engineering cases: the
skill passed every item, but the grader preferred the baseline's deeper
engineering detail (where the CI minutes go, fixing the slowest tests,
shadow runs, a wider cost margin). The skill's returned message was capped
at about 400 words, with the analysis moved to the full-plan file the
grader does not read.

## Change

`workflow/autonomous.md`:

- Stage 1 breaks the target metric into its parts (with rough figures and
  how to measure each) and looks for a bottleneck the obvious fix would not
  touch.
- The returned message keeps the action-first order but adds an execution
  section: measure first with decision rules, every lever from no-risk to
  risky (including expert fixes no principle points to), a path-to-target
  table with its margin, how to verify before switching, and deliverables.
- The 400-word cap is gone; length follows the work (usually 700-1,200
  words).

## Method

Same as the full run. The three autonomous cases were run again with the
skill (the two lost cases twice each, auto-thin-context once), and each new
run was graded blind against the same baseline transcript from the full run.
A/B order was varied (skill was A in 2 of 5).

## Results

| Run | With | Without | Preferred |
|---|---|---|---|
| auto-api-latency-vs-cost, run 1 | 10/10 | 9/10 | with |
| auto-api-latency-vs-cost, run 2 | 10/10 | 8/10 | with |
| auto-ci-speed-vs-coverage, run 1 | 11/11 | 6/11 | with |
| auto-ci-speed-vs-coverage, run 2 | 11/11 | 5/11 | with |
| auto-thin-context | 10/10 | 4/10 | with |

The skill was preferred in 5 of 5 runs, against 1 of 3 cases before. Its
answers are now about the baseline's length (1,100-1,500 words against
930-1,400). All four engineering runs carried a measure-first step, a
path-to-target table with its margin and a verification step (shadow run or
canary). Graders noted that both arms reached the same core fix; the skill
won on a quantified path, owned and dated steps, risk thresholds tied to
actions, and a stated confidence.

## Limits

- The baseline was not re-run, so its variance is not measured.
- The same model family played every role.
- Five runs; read it as a signal, not a benchmark.
