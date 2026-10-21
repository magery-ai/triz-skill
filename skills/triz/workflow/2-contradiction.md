# Stage 2: Find the contradiction

**Goal:** name the conflict at the root of the problem. A wrong contradiction
here makes every later stage solve the wrong problem.

## Steps

### 1. Build a cause chain

Start from the symptom the user described and ask "why does this happen?"
3-5 times. Write it as one line per link:

```
Reopen rate went from 8% to 19%
  because agents send replies before they understand the ticket
  because the 1-hour target leaves no time to investigate
  because every ticket gets the same target, simple or not
```

Stop at the first link the user can act on. Going deeper (to "because the
market is competitive") produces contradictions nobody can change.

### 2. Formulate the technical contradiction (TC)

> If we improve **A**, then **B** gets worse.

- **A** is what the user wants more of (or less of, for harm).
- **B** is what gets worse as a direct result. Check it with the user's own
  history: "when you pushed A, did B actually drop?"
- Also write the reverse: "If we protect B, then A stays bad." Both forms
  describe the same conflict; the reverse is useful when you look up the matrix
  in stage 3 because the cell for (B, A) can differ from (A, B).

### 3. Sharpen it into a physical contradiction (PC)

Find the one element that sits at the center of the conflict and the property
it needs two opposite values of:

> Element **E** must be **P** (to get A) and **not-P** (to avoid B).

Examples:

| TC | PC |
|----|----|
| Improving blade stiffness worsens weight | The blade must be thick (stiff) and thin (light) |
| Improving cache speed worsens data freshness | The cached value must stay (to be fast) and must change (to be fresh) |
| Improving reply speed worsens answer quality | The reply must be instant (fast) and considered (correct) |
| Improving fitness worsens free time | Exercise time must exist (for fitness) and must not exist (to keep free time) |

A PC is not always possible. If you cannot name a single element and property,
keep only the TC and say so.

### 4. Offer candidates when the problem is ambiguous

If the cause chain branches, or the user's words fit more than one conflict,
offer 2-3 candidate contradictions:

```
I see two possible conflicts:
1. Improving reply speed worsens answer quality. (Fits the reopen data best.)
2. Improving answer quality worsens agent workload.
Which one is closer to what you see, or is it something else?
```

Put the one that best explains the root cause first and say why.

## Checks before the gate

- The contradiction is about the **cause**, not the symptom.
- Improving A **really** worsens B; it is not just that both are bad.
- It is **one** contradiction. If you wrote "A worsens B and C", split it and
  pick the more important pair. Keep the other in open questions; it may come
  back in stage 4 as a secondary contradiction.
- A and B are both in the user's words. Parameter names come in stage 3.

## Common mistakes

- "We want it better and cheaper" is a wish, not a contradiction. Ask what
  happens to cost when quality goes up.
- Treating a constraint as B. "We can't hire" is a constraint; B is what gets
  worse because of it ("workload per agent").
- A trade-off that a simple optimization resolves. If a plain fix exists and
  nobody has tried it, say so; TRIZ may not be needed.

## Output

One chosen TC, its PC when found, and the cause chain. Update the state block.

## Gate

Ask the user to pick or correct the contradiction. Never skip this gate in
guided or fast mode. If the user rejects all candidates, ask what conflict they
feel and rebuild from their answer.
