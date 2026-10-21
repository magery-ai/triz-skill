# Autonomous mode

Use this mode when no human can answer: a coding agent stuck on a design
trade-off, a subagent called by an orchestrator, a batch job. It starts when
the caller asks for it, or when you have no way to ask anyone.

The six stages stay the same. What changes is who answers the gates.

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

Write both plans as in `workflow/6-plan.md`, with the Assumptions section and
the confidence level filled in. Return the short plan to the caller and the
path of the full plan.

If confidence is **low**, put "Needs human review" at the top of both plans and
do not act on the plan yourself, even if the caller allowed it. Tell the caller
which assumption or finding a human should check first.
