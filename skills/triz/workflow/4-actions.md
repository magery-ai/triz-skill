# Stage 4: Turn directions into concrete actions

**Goal:** turn each direction into actions the user can actually take, then
rank them so the user sees the best 2-3 first.

## Steps

### 1. Write actions for each direction

For each principle from stage 3, write 1-3 actions. Use the principle's
sub-principles and domain examples (`--principle <id>`) as prompts, then
rewrite them in the user's situation. Each action says:

- **Who** does it (a person, team, role, or the system itself).
- **What** they do, as a verb and an object.
- **With what**: a resource from stage 1.
- **What it changes**: the effect on A and on B.

Good: "Seniors write Zendesk macros for the 20 most common ticket types, using
last quarter's ticket history (#10). Replies to those tickets become instant
without dropping quality."

Bad: "Apply preliminary action to support." (restates the principle)

### 2. Filter

Drop an action when:

- it only restates the principle;
- it breaks a constraint or changes something the user said must not change;
- it uses a resource the user does not have;
- it is the fix the user already tried, unless you change why it failed.

If a direction produces no surviving action, drop the direction and say so in
one line.

### 3. Score

| Score | High | Medium | Low |
|-------|------|--------|-----|
| **IFR fit** | Gets close to the IFR; the system does it largely by itself | Clear improvement, but needs ongoing effort | Small or partial improvement |
| **Effort** | New budget, people or months of work | Some work from existing people, weeks | Hours or days with what is already there |
| **Side effects** | Note any new problem the action creates; "none seen" is allowed but think first | | |

A side effect that is "improving C worsens D" is a **secondary contradiction**.
Record it for the plan's Risks section; do not solve it now unless it kills the
action.

### 4. Rank and recommend

Rank by IFR fit first, then by low effort, then by fewest side effects.
Recommend the top 2-3. Actions that combine well (one handles the common case,
another the rest) can be recommended together as one option.

## Output

```
Options, ranked:
1. <action> (#<n>). IFR fit: high. Effort: low. Side effects: <...>
2. <action> (#<n>). IFR fit: high. Effort: medium. Side effects: <...>
3. ...
Recommended: 1 and 2 together, because <reason>.
```

Update the state block with the recommended option. There is no gate; stage 5
is where the user tests the options.

## If the user adds a constraint later

When stage 5 reveals a constraint you did not know, come back here: add it to
the state block, re-run the filter on the existing actions, and re-rank.
Do not repeat stages 1-3.
