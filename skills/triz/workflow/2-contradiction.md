# Stage 2: Find the contradiction

> Draft for v0.1. Expanded in v0.3.

**Goal:** name the conflict at the root of the problem.

## Steps

1. Build a short cause chain from the symptom down to its root cause
   (3-5 links, each "because ...").
2. Formulate a technical contradiction: "If we improve A, then B gets worse."
3. Sharpen it into a physical contradiction where possible:
   "Element E must be P (to get A) and not-P (to avoid B)."
4. If the problem is ambiguous, offer 2-3 candidate contradictions and say
   which one you think explains the root cause best.

## Pitfalls

- A contradiction about the symptom instead of the cause.
- "A vs B" where B is not actually worsened by improving A.
- Mixing two contradictions into one.

## Output

One chosen technical contradiction and, when found, its physical contradiction.

## Gate

The user picks or corrects the contradiction. A wrong pick here invalidates
everything after it, so never skip this gate in guided or fast mode.
