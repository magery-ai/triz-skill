# Stage 5: Validate with Socratic questions

> Draft for v0.1. The full question bank (about 30 questions) arrives in v0.3.

**Goal:** test the top options with the user before committing to one.

## Steps

1. Present the top options briefly.
2. Ask one question at a time, drawn from these types:
   - **Clarification:** "What do you mean by ...?"
   - **Assumptions:** "What are we assuming must stay the same?"
   - **Evidence:** "What tells you this would work here?"
   - **Viewpoints:** "Who would object, and why?"
   - **Consequences:** "What new problem does this create?"
   - **The question itself:** "Is this still the problem you want solved?"
3. Stop when the user approves an option, or after about 7 questions.

## Loop-back rules

- The answers reveal a new contradiction: go back to stage 2 with it.
- The answers reveal a missing constraint: go back to stage 4.

## Fast mode

Ask only 2-3 risk questions (consequences, viewpoints). The user may skip this
stage entirely; note "not validated" in the plan if they do.

## Output

The approved option plus the objections raised and how they were answered.

## Gate

Explicit user approval.
