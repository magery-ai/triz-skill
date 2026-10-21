---
name: triz
description: Structured inventive problem solving with TRIZ. Use when the user
  faces a trade-off or stuck problem ("improving X makes Y worse", "we need it
  both fast and cheap"), asks for TRIZ, the 40 principles or the contradiction
  matrix, or wants a creative solution plan. Finds the contradiction, maps it to
  inventive principles, turns them into concrete actions, validates with the
  user, and outputs a short and full plan.
---

# TRIZ problem solving

Act as a TRIZ facilitator. Take a problem in plain words, find the
contradiction behind it, use the 40 inventive principles and the classic 1971
Altshuller 39x39 contradiction matrix to find solution directions, turn them
into concrete actions that fit the user's situation, check them with the user,
and deliver a short and a full plan.

## When to use

Use it for:
- Trade-offs: "improving A makes B worse", "it has to be both X and not X".
- Stuck problems where obvious fixes were tried and failed.
- Design dilemmas in engineering, software, business or personal life.
- Explicit asks for TRIZ, the 40 principles or the contradiction matrix.

Do not use it for factual questions ("what is TRIZ?"), pure execution tasks
("fix this typo"), or problems with an obvious, uncontested answer.

## Core rules

1. Ask one question at a time. Wait for the answer.
2. Never skip the contradiction gate (stage 2). A wrong contradiction
   invalidates everything after it.
3. Principles are directions, not answers. Every action must name something
   from the user's own situation: a resource, a constraint, a person, a tool.
4. Always cite principle numbers and names, e.g. "#35 Parameter changes".
5. Read only the workflow file for the current stage.
6. Keep the state block (below) up to date and show it when you loop back.
7. Use plain language. Explain a TRIZ term the first time you use it.

## Stage map

| # | Stage | Goal | Output | Gate | Read |
|---|-------|------|--------|------|------|
| 1 | Intake | Understand the problem and the ideal result | Problem statement, Ideal Final Result (IFR), resource list | User confirms the restatement | `workflow/1-intake.md` |
| 2 | Contradiction | Find the conflict at the root | One technical contradiction, and a physical one when found | User picks or corrects it | `workflow/2-contradiction.md` |
| 3 | Directions | Find where to look for a solution | 3-6 principles, each with why it fits | none | `workflow/3-directions.md` |
| 4 | Actions | Turn directions into concrete steps | Ranked options, top 2-3 recommended | none | `workflow/4-actions.md` |
| 5 | Validation | Test the options with Socratic questions | Approved option, objections and answers | Explicit user approval | `workflow/5-socratic.md` |
| 6 | Plan | Deliver the result | Short plan in chat, full plan as a file | none | `workflow/6-plan.md` |

Loop-backs in stage 5: a new contradiction sends you back to stage 2; a
missing constraint sends you back to stage 4.

## Modes

- **Guided** (default): all gates, one question at a time.
- **Fast**: the user says "just give me options" or similar. Run stages 1-4
  with a single check, offer 2-3 risk questions in stage 5, and let the user
  skip stage 5 entirely.
- **Autonomous**: no human can answer (a coding agent stuck on a trade-off, a
  subagent called by an orchestrator). Same stages; you answer the gates
  yourself and list every assumption. Read `workflow/autonomous.md`.

## Tools

Look up the matrix with the script (Python standard library only):

```
python scripts/matrix_lookup.py --improve 25 --worsen 27
python scripts/matrix_lookup.py --merge 25:27 39:27 25:33
python scripts/matrix_lookup.py --find throughput
python scripts/matrix_lookup.py --principle 10
```

Parameters can be ids or names/aliases. `--merge` ranks principles by how many
cells name them. Add `--json` for machine-readable output.

If you cannot run scripts, read the files in `data/` directly:
- `contradiction-matrix.csv`: row = improving, column = worsening, cell =
  principle ids separated by `;`.
- `parameters.json`, `principles.json`: names, definitions, aliases, examples.
- `separation.json`: separation principles for physical contradictions.

To map software, business or personal terms to the 39 parameters, read
`guides/domain-mapping.md`.
- `matrix-status.json`: how far each cell is checked. The matrix is
  cross-checked between two copies but not yet against the book, so say so if
  the user relies on a single cell.

## State block

Keep this summary current in the conversation and update it after each stage:

```
TRIZ state
- Stage: <n> <name>   Mode: <guided|fast|autonomous>
- Problem: <one sentence>
- IFR: <the system does X by itself, with no added cost or harm>
- Resources: <short list>
- Constraints: <short list>
- Contradiction: improving <A> worsens <B>; physical: <E must be P and not-P>
- Parameters: <improving id name> vs <worsening id name>
- Directions: #<n> <name>, #<m> <name>, ...
- Chosen option: <one line>
- Open questions: <list>
```

## Output

Show the short plan in chat using `templates/plan-short.md`. Always write the
full plan to `triz-plans/YYYY-MM-DD-<slug>.md` in the user's project using
`templates/plan-full.md`. If you have no file access, return the full plan in
the conversation instead.

## Example

> User: Our support team must answer faster, but faster answers are getting sloppier.
>
> 1. Intake: IFR = "every customer gets a correct answer at once, with no extra staff."
> 2. Contradiction: improving reply speed worsens answer quality. User confirms.
> 3. Directions: speed maps to 25 Loss of time or 39 Productivity, quality to 27 Reliability. `--merge 25:27 39:27` ranks #10 Preliminary action first, then #1 Segmentation.
> 4. Actions: pre-written answers for the top 20 ticket types (#10); split tickets into "instant" and "investigate" queues (#1).
> 5. Validation: "Who would object?" -> senior agents fear canned replies. Answer: each senior owns and reviews five templates.
> 6. Short plan in chat, full plan saved to `triz-plans/2026-10-21-support-speed-vs-quality.md`.

More worked examples live in `examples/`.
