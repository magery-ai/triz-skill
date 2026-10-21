# Stage 6: Deliver the plan

**Goal:** give the user something to act on now (the short plan) and a record
of why (the full plan).

## Steps

1. **Fill `templates/plan-short.md`** and show it in chat.
   - Keep it on one screen: at most 3-5 next steps.
   - Every step has an owner and a time ("by Friday", "in 2 weeks"). If the
     user did not say, propose one and mark it "(proposed)".
   - "Watch for" names the top risk and the signal that it is happening.
   - "Done when" is measurable and tied to the IFR.
2. **Fill `templates/plan-full.md`** from the state block and the stage
   outputs. Fill every section; write "none" rather than deleting a section.
   - Directions considered: list every principle from stage 3, including
     those whose actions were dropped, so the user can come back to them.
   - Options and scoring: every action from stage 4 with its scores.
   - Validation log: every question from stage 5, or "skipped (fast mode)".
   - Risks and fallbacks: secondary contradictions from stage 4, each with the
     next principle to try.
3. **Save the full plan** to `triz-plans/YYYY-MM-DD-<slug>.md` in the user's
   project. Create the folder if needed.
   - Date: today.
   - Slug: the problem in 3-6 lowercase words joined by hyphens, letters,
     digits and hyphens only, e.g. `support-speed-vs-quality`.
   - If the file exists, add `-2`, `-3`, and so on.
4. **Tell the user** where the full plan was saved, in one line.

If you have no file access, show the full plan in the conversation after the
short one and say that it was not saved.

## Autonomous mode

Also fill the Assumptions section and the confidence level (see
`workflow/autonomous.md`). Set "Validated: critic pass (autonomous)". If
confidence is low, put "Needs human review" at the top of both plans.

## After delivery

Offer one follow-up in a single line, for example: "Want me to work on the
secondary contradiction (<C> vs <D>) next?" Do not start it unless asked.
