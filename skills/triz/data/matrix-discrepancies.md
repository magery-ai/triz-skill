# Matrix discrepancies

Cells where the copies of the classic 39x39 matrix disagree. When the copies
disagree, `contradiction-matrix.csv` holds the triz40.com value until the book
settles it; the book (Altshuller, *40 Principles*, Shulyak and Rodman
translation, 1997) wins once it has been checked. Cell status lives in
`matrix-status.json`.

Cell ids are `improving-worsening`.

## Cross-check of 2026-10-21

Compared all 1,521 cells (39 x 39) of triz40.com against the copy in pytriz
0.4.0 (identical to triz-mcp). Both have 1,248 filled cells and the same
empty cells and diagonal.

| Cell | Parameters | triz40.com | Other copy | Outcome |
|------|------------|------------|------------|---------|
| 19-9 | Use of energy by moving object / Speed | 8, 35 | 8, 35, 35 | Same principles; the other copy repeats 35, a typo. Kept 8, 35. Status: cross-checked. |

No other differences, including the order of principles inside each cell.

## Book check

Not started. Planned for v1.0. Until then `matrix-status.json` has
`"book_verified": false` and no cell is marked `verified`.
