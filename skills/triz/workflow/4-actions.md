# Stage 4: Turn directions into concrete actions

**Goal:** turn each direction into actions the user can actually take, then
rank them so the user sees the best 2-3 first.

## Steps

### 0. List the expert levers first

Before using the principles, write down the 2-4 quantities that drive A and B
in this domain, the way an experienced practitioner would check them first.
Give a rough number for each where you can (current value, what is
achievable). Examples: for drone flight time, battery energy density, hover
power per kg and motor efficiency; for CI time, the slowest jobs, queue wait
and test parallelism; for stock, carrying cost and lead time.

These levers are not the answer either. Use them in step 1: the best actions
apply a principle to one of these levers. If an obvious expert fix exists that
no principle points to, keep it as an option and say so; TRIZ is there to find
better options, not to hide good ones.

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

### 3. Check the numbers against the target

For each surviving action, estimate how far it moves the user's target (the
IFR metric from stage 1), even roughly: "about +4 minutes of flight", "cuts
the 42 minutes by about half". Say what the estimate rests on.

If no single action reaches the target, show which combination does. If none
does, say how far short the best combination falls.

Do not lower the user's target (a smaller payload, a looser deadline) to make
an option work unless the user agreed to that change. Lowering the target is
the compromise TRIZ tries to avoid; offer it only as a labelled fallback.

### 4. Score

| Score | High | Medium | Low |
|-------|------|--------|-----|
| **IFR fit** | Gets close to the IFR; the system does it largely by itself | Clear improvement, but needs ongoing effort | Small or partial improvement |
| **Effort** | New budget, people or months of work | Some work from existing people, weeks | Hours or days with what is already there |
| **Side effects** | Note any new problem the action creates; "none seen" is allowed but think first | | |

A side effect that is "improving C worsens D" is a **secondary contradiction**.
Record it for the plan's Risks section; do not solve it now unless it kills the
action.

### 5. Rank and recommend

Rank by IFR fit first (does it reach the target, by the estimate in step 3),
then by low effort, then by fewest side effects.
Recommend the top 2-3. Actions that combine well (one handles the common case,
another the rest) can be recommended together as one option.

## Output

```
Options, ranked:
1. <action> (#<n>). Moves target by: <estimate>. IFR fit: high. Effort: low. Side effects: <...>
2. <action> (#<n>). Moves target by: <estimate>. IFR fit: high. Effort: medium. Side effects: <...>
3. ...
Recommended: 1 and 2 together, because <reason>.
```

Update the state block with the recommended option. There is no gate; stage 5
is where the user tests the options.

## If the user adds a constraint later

When stage 5 reveals a constraint you did not know, come back here: add it to
the state block, re-run the filter on the existing actions, and re-rank.
Do not repeat stages 1-3.
