# Stage 3: Find solution directions

**Goal:** find 3-6 inventive principles that point toward a solution, each with
a reason it fits this problem.

Run both lookups when you have both a technical and a physical contradiction,
then combine the results.

## Technical contradiction: the matrix

### 1. Map A and B to parameters

Map A (improving) and B (worsening) to the 39 parameters in
`data/parameters.json`.

- For engineering problems the names usually fit directly.
- For software, business and personal problems use
  `guides/domain-mapping.md`.
- `python scripts/matrix_lookup.py --find <term>` searches names and aliases.

Say how sure you are. If one parameter clearly fits, use it. If two or three
fit, keep them all for step 3.

### 2. Read the cell

```
python scripts/matrix_lookup.py --improve <A> --worsen <B>
```

Or read `data/contradiction-matrix.csv`: row = improving, column = worsening,
cell = principle ids separated by `;`, in the matrix's own order.

- An **empty cell** means the matrix has no suggestion for that pair. Follow
  the empty-cell rule below.
- The **diagonal** is always empty: the same parameter on both sides is a
  physical contradiction. Use separation below.
- Check the cell's status in the output. Most cells are "cross-checked":
  three copies agree, but none has been checked against the book. A
  "disputed" cell has a different value in the 1973 Altshuller table; look it
  up in `data/matrix-discrepancies.md`, tell the user both values, and
  consider principles from both.

### Empty-cell rule

When the cell is empty, work through these steps in order and stop at the
first one that gives principles:

1. **Reverse.** Read the reverse cell (B improving, A worsening). If it has
   principles, use them and say so: "The direct cell is empty; the reverse
   cell gives ...".
2. **Say it plainly.** If both are empty, tell the user: "The matrix has no
   principles for <A id name> vs <B id name>, in either direction."
3. **Neighbour.** Swap one side for its closest neighbour from
   `guides/domain-mapping.md` (Neighbours for empty cells), and read the
   direct and reverse cells again. Change one side at a time, and keep a
   neighbour only if it still describes the user's problem.
   - Guided: ask in one line, "Shall I read cost as 23 Loss of substance
     (money spent while running) instead? That cell has principles." This is
     the only question stage 3 may ask.
   - Fast: state the swap in one line and go on.
   - Autonomous: make the swap and record it as an assumption.
4. **Separation only.** If no neighbour fits, or every fitting cell is empty,
   take the directions from separation alone and say so in the output.

Never invent principles for an empty cell, and never fill it from a
neighbour without saying which neighbour you used.

### 3. Merge when the mapping is uncertain

```
python scripts/matrix_lookup.py --merge 25:27 39:27 25:29
```

Principles that appear in more than one cell rank higher. Prefer them, but do
not drop a single-cell principle that obviously fits.

## Physical contradiction: separation

Ask each separation question about the element E and the property P. Use
`data/separation.json` for the principles linked to each type.

| Separation | Question | Look for |
|------------|----------|----------|
| Time | Can E be P at one moment and not-P at another? | The two needs happen at different times |
| Space | Can E be P in one place and not-P in another? | The two needs happen in different places or parts |
| Condition | Can E be P under one condition and not-P under another? | The need depends on who, what or which case |
| System level | Can the whole be P while its parts are not-P, or the reverse? | One level can have P while another has not-P |

Most problems fit one or two types well. Name the one that fits best and pick
the 1-3 principles from its list that suggest something concrete.

## Choosing the directions

1. Start with principles that appear in both the matrix and a fitting
   separation type.
2. Add the strongest remaining matrix principles, in cell order.
3. Stop at 6. Fewer good directions beat many weak ones.
4. For each, read its sub-principles and domain examples in
   `data/principles.json` (`--principle <id>`) and write one line on why it
   fits this problem. If you cannot write that line, drop the principle.

A principle that sounds physical (#29 Pneumatics and hydraulics, #36 Phase
transitions, #38 Strong oxidants) can still be useful outside engineering as an
analogy. Read its software, business and everyday examples before dropping it,
but do not stretch an analogy past what the user would find natural.

## Output

```
Matrix: improving <id name> vs worsening <id name> -> #a, #b, #c, #d [status]
  (or: empty both ways; neighbour <id name> -> #a, #b [status])
  (or: empty both ways and for neighbours; directions from separation only)
Separation: <type>, because <reason>
Directions:
1. #<n> <name>: <why it fits, in the user's terms>
2. ...
```

Update the state block. There is no gate here; go straight to stage 4. In
guided mode you may show the directions briefly before the actions.
