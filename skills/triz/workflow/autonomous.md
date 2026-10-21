# Autonomous mode

> Draft for v0.1. Expanded in v0.3.

Use this mode when no human can answer: a coding agent stuck on a design
trade-off, or a subagent called by an orchestrator. It starts when the caller
asks for it or when no user can answer. The stages stay the same; what changes
is who answers.

| Stage | Guided | Autonomous |
|-------|--------|------------|
| 1 Intake | Ask the user clarifying questions | Read the context you already have (task, code, files); list every gap you filled as an assumption |
| 2 Contradiction gate | User picks | Rank 2-3 candidates by how well they explain the root cause; pick one and say why |
| 3-4 Directions, actions | Same | Same, but every action must use a resource you can actually see |
| 5 Socratic validation | User answers | Self-critique pass, or a separate critic agent answers the question bank adversarially; an option survives only if it has an answer to every question type |
| Loop-backs | On user answers | On critic findings, capped at 2 loops |
| 6 Plan | Short in chat, full as a file | Both, plus an Assumptions section and a confidence level (high, medium, low) |

If confidence ends low, return the plan flagged "needs human review" instead of
acting on it.
