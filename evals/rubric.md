# Scenario rubric

Grade each run of a case in `cases/` against these items. Each item is pass or
fail; write one line of evidence from the transcript for every fail.

## All modes

| Item | Pass when |
|------|-----------|
| Contradiction | The chosen contradiction matches one in `expected_contradictions`, stated as "improving A worsens B" |
| Gate respected | Guided: the agent asked for confirmation of the restatement and the contradiction before stage 3, separately or merged into one turn when stage 1 left nothing open. Fast: one combined check before stage 3 |
| Question budget | Guided: at most 2 clarifying questions in stage 1 and 2 Socratic questions in stage 5, one per turn, unless the persona asked for more or a loop-back needed it; the plan arrives within 8 user turns otherwise. Fast: at most 1 clarifying question and 2 risk questions |
| Correct lookup | Principles cited for the matrix match the cell for the parameters the agent named (`matrix_lookup.py` output) |
| Context use | Every top action names a resource or constraint from the conversation or context |
| Socratic validation | Guided: 2 questions of different types, one at a time, then an approval request. Fast: validation offered and skippable |
| Loop-back | When the persona raises a new conflict or constraint, the agent returns to stage 2 or 4 |
| Output | The short plan follows `templates/plan-short.md`; the full plan is saved or shown |
| Plan fields | Both plans have Resources (existing and new, or "nothing new"), Watch for (a signal with a number or yes/no fact, and an action) and Done when (a metric, a target and a date or window). Vague entries like "quality drops" fail |
| Case checks | Every line in the case's `checks` holds |

## Autonomous mode, in addition

| Item | Pass when |
|------|-----------|
| Assumptions | Every gap filled without evidence is listed as an assumption with its impact |
| Critic pass | The critic pass answers all six question types for the top option |
| Loop cap | No more than 2 loop-backs |
| Confidence | A confidence level is stated, and a low level comes with "Needs human review" and no action taken |

## Scoring

A run passes when every item passes. Track the pass rate per item across
cases: the item that fails most often points at the stage file to improve.
