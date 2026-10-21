# Autonomous mode

Use this mode when no human can answer: a coding agent stuck on a design
trade-off, a subagent called by an orchestrator, a batch job. It starts when
the caller asks for it, or when you have no way to ask anyone.

The six stages stay the same. What changes is who answers the gates. The
question budget in SKILL.md does not apply, since questions cost no one's
time: the critic pass answers all six question types. The required plan
fields (Resources, Watch for, Done when) still apply.

| Stage | Guided | Autonomous |
|-------|--------|------------|
| 1 Intake | Ask the user clarifying questions | Read the context you already have; list every gap you filled as an assumption |
| 2 Contradiction gate | User picks | Rank 2-3 candidates; pick one and say why |
| 3-4 Directions, actions | Same | Same, but every action must use a resource you can actually see |
| 5 Socratic validation | User answers | Critic pass: an option survives only if it answers every question type |
| Loop-backs | On user answers | On critic findings, at most 2 loops |
| 6 Plan | Short in chat, full as a file | Both, plus Assumptions and a confidence level |

## Stage 1: intake from context

Read what you have: the task, code, files, logs, tickets, earlier messages.
Answer the intake questions yourself. For each answer you could not ground in
something you read, add an assumption:

```
A1. <assumption>. Basis: <what made you think so, or "none">. Impact if wrong: <high|medium|low>
```

Write the IFR and resources as usual. Only list resources you can point to.

### Break the metric down

Before you look for the contradiction, split the number the caller wants to
move into the parts that add up to it, the way a practitioner would on day
one: where the 42 minutes of CI go (queue, setup, build, each test suite,
the slowest single tests), which part of the 600 ms is queueing and which is
work, which segment the lost sales come from. Give a rough figure for each
part, mark it as an estimate or as read from context, and name the file,
log or query that would measure it.

Look for a bottleneck the obvious fix would not touch (a database behind the
replicas, one test longer than any shard). If one exists, it goes into the
plan, even if no principle points to it.

## Stage 2: pick the contradiction

Write 2-3 candidates and rank them on:

1. **Explains the root:** does it explain the symptom through the cause chain?
2. **Actionable:** can the caller change A or B?
3. **Evidence:** is it grounded in what you read, not in assumptions?

Pick the top one, record the others, and state why in one line.

## Stage 5: the critic pass

Run it as a separate step after stage 4, in one of two ways:

- **Self-critique:** switch roles. Read the options as a skeptic whose job is to
  find why each one fails. Answer at least one question of each of the six
  types in `workflow/5-socratic.md` for each top option.
- **Critic agent:** if you can start a subagent, give it the state block, the
  top options and the question bank, and this instruction: "For each option,
  answer one question of each type as a skeptic. Say which option fails and
  why." Then answer its findings yourself.

An option **survives** only if every question type has an answer that does not
kill it. Record each finding and your answer in the validation log.

Loop back as in guided mode (new contradiction to stage 2, missing constraint to
stage 4), but stop after **2 loops**. After that, take the best surviving
option, or the best option overall if none survived, and lower the confidence.

## Confidence

| Level | When |
|-------|------|
| High | The contradiction is grounded in evidence, the winning option survived the critic pass, and no high-impact assumption is unverified |
| Medium | The option survived, but at least one high-impact assumption is unverified, or the parameter mapping was uncertain |
| Low | No option fully survived, the loop cap was hit, or the contradiction rests mostly on assumptions |

## Output

The caller is usually another agent that will carry out your answer without
asking anything. Give it enough engineering detail to do the work: an
experienced engineer handed the message should not have to redo your
analysis. Lead with what to do, and keep the TRIZ analysis in the full plan.

Write both plans as in `workflow/6-plan.md`, with the Assumptions section and
the confidence level filled in. Return this to the caller, in this order:

1. **Confidence**, and "Needs human review" if it is low.
2. **The short plan** (`templates/plan-short.md`), with all three required
   fields. In autonomous mode the next steps may run past 5 when the work
   needs them.
3. **Execution detail.** This is where the plan earns its keep:
   - **Measure first.** The breakdown from stage 1 as a step: what to read
     or run, what to compute, and which number decides between branches of
     the plan ("if e2e is under 15 of the 42 minutes, skip step 4").
   - **Every lever, cheapest first.** Order the steps from no-risk to risky.
     Include the expert levers from stage 4 that the principles did not point
     to (caching, fixing the slowest few tests, query fixes, quarantining
     flaky tests) when they move the target. Name the files, commands,
     config keys, tools or queries for each step.
   - **Path to target.** A small table from today's value to the target:
     each step, its estimated effect and what the estimate rests on. Show the
     margin at the end. If the plan only just reaches the target (less than
     about 20% headroom), add the next lever or say plainly that the margin
     is thin.
   - **Verify before switching.** How the caller proves the change works
     before it becomes the default: a shadow run beside the old setup, a
     canary, a dry run, a holdout. Say what result counts as a pass.
   - **Deliverables:** the files, PRs or reports the caller should produce.
4. **Safety fallback:** what to do if a step makes things worse (how to roll
   back or what to keep running).
5. **Assumptions** with high impact, one line each, and the step that checks
   each one.
6. **Critic pass**, in one line: that all six question types were answered,
   and what the pass changed or rejected.
7. The path of the full plan.

Length follows the work: a plan with real engineering steps usually runs
700-1,200 words; a low-confidence plan with little context can be shorter.
Do not pad, and do not cut a step the caller needs to act. Leave the
contradiction ranking, matrix lookups and critic log out of the returned
message; they belong in the full plan. If you cannot write files, put them
after the seven parts above under "Analysis".

If confidence is **low**, put "Needs human review" at the top of both plans and
do not act on the plan yourself, even if the caller allowed it. Tell the caller
which assumption or finding a human should check first.
