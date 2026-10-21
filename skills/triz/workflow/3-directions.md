# Stage 3: Find solution directions

> Draft for v0.1. Data files and the lookup script arrive in v0.2.

**Goal:** find 3-6 inventive principles that point toward a solution.

## Technical contradiction: the matrix

1. Map A (improving) and B (worsening) to the 39 engineering parameters.
   For non-engineering problems use `guides/domain-mapping.md` (v0.3).
2. Read the matrix cell (row = improving, column = worsening) to get 1-4
   principle numbers.
3. If the mapping is uncertain, try the 2-3 closest parameter pairs and merge
   the results. Rank principles that appear more than once higher.

## Physical contradiction: separation

Try each separation principle and ask its question:

- **Time:** can E be P at one moment and not-P at another?
- **Space:** can E be P in one place and not-P in another?
- **Condition:** can E be P under one condition and not-P under another?
- **System level:** can the whole be P while its parts are not-P, or the reverse?

## Output

3-6 directions, each as principle number + name + one line on why it fits.
