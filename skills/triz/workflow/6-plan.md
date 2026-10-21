# Stage 6: Deliver the plan

**Goal:** give the user something to act on now (the short plan) and a record
of why (the full plan).

## Steps

1. **Fill `templates/plan-short.md`** and show it in chat.
   - Keep it on one screen: at most 3-5 next steps (autonomous mode can
     use more; see `workflow/autonomous.md`).
   - Every step has an owner and a time ("by Friday", "in 2 weeks"). If the
     user did not say, propose one and mark it "(proposed)".
   - Fill the three required fields (see below): Resources, Watch for and
     Done when.
2. **Fill `templates/plan-full.md`** from the state block and the stage
   outputs. Fill every section; write "none" rather than deleting a section.
   - Directions considered: list every principle from stage 3, including
     those whose actions were dropped, so the user can come back to them.
   - Options and scoring: every action from stage 4 with its scores.
   - Validation log: every question from stage 5, or "skipped (fast mode)".
   - Risks and fallbacks: secondary contradictions from stage 4, each with the
     next principle to try.
   - Section 9: the same three required fields, in more detail.
3. **Save the full plan** to `triz-plans/YYYY-MM-DD-<slug>.md` in the user's
   project. Create the folder if needed.
   - Date: today.
   - Slug: the problem in 3-6 lowercase words joined by hyphens, letters,
     digits and hyphens only, e.g. `support-speed-vs-quality`.
   - If the file exists, add `-2`, `-3`, and so on.
4. **Tell the user** where the full plan was saved, in one line.

## Required fields

Every plan, short and full, in every mode, has these three fields. They turn
the plan into something anyone can check later without asking for an opinion.

| Field | Must contain | Good | Not enough |
|-------|--------------|------|------------|
| **Resources** | What the plan uses from the stage 1 list, and anything new with its cost. Write "nothing new" when that is true | "Zendesk macros, ticket history, seniors' time (2 h each); new: nothing" | "the team" |
| **Watch for** | The top risk, a signal with a number or a yes/no fact, and what to do when it is crossed | "reopen rate on macro tickets above 8% for a week: pull that macro for review" | "quality drops" |
| **Done when** | A metric tied to the IFR, a target and a date or time window | "median first reply under 1 h and reopen rate at or below 8%, by end of Q1" | "customers are happier" |

Before you deliver, check each field against the "Must contain" column. If a
number is unknown, propose one and mark it "(proposed)", and add the question
to open questions. Never leave a field out or write "n/a".

If you have no file access, show the full plan in the conversation after the
short one and say that it was not saved.

## Autonomous mode

Also fill the Assumptions section and the confidence level (see
`workflow/autonomous.md`). Set "Validated: critic pass (autonomous)". If
confidence is low, put "Needs human review" at the top of both plans.

## After delivery

Offer one follow-up in a single line, for example: "Want me to work on the
secondary contradiction (<C> vs <D>) next?" Do not start it unless asked.
