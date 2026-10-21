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
| 19-9 | Use of energy by moving object / Speed | 8, 35 | 8, 35, 35 | Same principles; the other copy repeats 35, a typo. Kept 8, 35. Now disputed: the 1973 table has 8, 15, 35 (see below). |

No other differences, including the order of principles inside each cell.

## Third source: Altshuller Foundation, 1973 table (2026-10-21)

Compared all 1,521 cells against the table on the official site of the
G.S. Altshuller Foundation,
<https://www.altshuller.ru/triz/technique2.asp>, which cites Altshuller,
*Алгоритм изобретения* (Algorithm of Invention), Moscow, Moskovsky Rabochy,
1973, Appendix 1. Its origin is documented and it does not depend on
triz40.com.

How it was read: the page was fetched and transcribed cell by cell twice, by
separate readers, and every cell that differed from the CSV was read again.
The page's text drops some empty-cell dashes, glues a few cells together and
uses a period as a separator in places; where a block had a missing dash, the
cells were matched by their order instead of their column. Every value below
was the same in both readings. Treat the 1973 values as a careful
transcription of a web page, not as a check against print.

Result:

- **1,482 cells agree** with `contradiction-matrix.csv`, including every empty
  cell except one.
- **10 cells** have the same principles in a different order (table below).
  Their status stays `cross-checked`; the CSV order is kept.
- **29 cells** differ in content. Most differ by one number (for example 25
  instead of 35, or 6 instead of 26), which looks like typos in one copy or
  the other. These cells are marked `disputed` in `matrix-status.json`, and
  the CSV keeps the triz40.com value, which the second copy also has, until
  the book settles it.

### Content differences

| Cell | Parameters | CSV (triz40.com and pytriz) | 1973 table | Outcome |
|------|------------|-----------------------------|------------|---------|
| 2-29 | Weight of stationary object / Manufacturing precision | 10, 1, 35, 17 | 10, 1, 35, 27 | Disputed. |
| 4-16 | Length of stationary object / Duration of action by stationary object | 1, 10, 35 | 1, 40, 35 | Disputed. |
| 5-11 | Area of moving object / Stress or pressure | 10, 15, 36, 28 | 10, 35, 36, 28 | Disputed. |
| 9-1 | Speed / Weight of moving object | 2, 28, 13, 38 | 8, 28, 13, 38 | Disputed. |
| 9-29 | Speed / Manufacturing precision | 10, 28, 32, 25 | 10, 28, 32, 35 | Disputed. |
| 12-11 | Shape / Stress or pressure | 34, 15, 10, 14 | 34, 35, 10, 14 | Disputed. |
| 12-19 | Shape / Use of energy by moving object | 2, 6, 34, 14 | 2, 26, 34, 14 | Disputed. |
| 13-18 | Stability of the object's composition / Illumination intensity | 32, 3, 27, 16 | 32, 3, 27, 15 | Disputed. |
| 14-33 | Strength / Ease of operation | 32, 40, 25, 2 | 32, 40, 28, 2 | Disputed. |
| 14-36 | Strength / Device complexity | 2, 13, 25, 28 | 2, 13, 28 | Disputed. |
| 15-36 | Duration of action of moving object / Device complexity | 10, 4, 29, 15 | 10, 4, 28, 15 | Disputed. |
| 17-23 | Temperature / Loss of substance | 21, 36, 29, 31 | 21, 36, 39, 31 | Disputed. |
| 18-22 | Illumination intensity / Loss of energy | 13, 16, 1, 6 | 19, 16, 1, 6 | Disputed. |
| 19-9 | Use of energy by moving object / Speed | 8, 35 | 8, 15, 35 | Disputed. The pytriz copy has 8, 35, 35, which fits a lost 15. |
| 21-12 | Power / Shape | 29, 14, 2, 40 | 29, 14, 3, 40 | Disputed. |
| 21-23 | Power / Loss of substance | 28, 27, 18, 38 | 28, 37, 18, 38 | Disputed. |
| 25-5 | Loss of time / Area of moving object | 26, 4, 5, 16 | 28, 4, 5, 16 | Disputed. |
| 26-27 | Quantity of substance / Reliability | 18, 3, 28, 40 | 3, 2, 28 | Disputed. |
| 28-31 | Measurement accuracy / Object-generated harmful factors | 3, 33, 39, 10 | 3, 3, 29, 10 | Disputed. The 1973 page repeats 3, so it has a typo of its own. |
| 29-7 | Manufacturing precision / Volume of moving object | 32, 23, 2 | 32, 28, 2 | Disputed. |
| 29-22 | Manufacturing precision / Loss of energy | 13, 32, 2 | 13, 22, 2 | Disputed. |
| 32-4 | Ease of manufacture / Length of stationary object | 15, 17, 27 | 13, 17, 27 | Disputed. |
| 35-37 | Adaptability or versatility / Difficulty of detecting and measuring | 1 | empty | Disputed. |
| 35-39 | Adaptability or versatility / Productivity | 35, 28, 6, 37 | 35, 26, 6, 37 | Disputed. |
| 36-10 | Device complexity / Force | 26, 16 | 26, 18 | Disputed. |
| 37-10 | Difficulty of detecting and measuring / Force | 30, 28, 40, 19 | 36, 28, 40, 19 | Disputed. |
| 37-21 | Difficulty of detecting and measuring / Power | 18, 1, 16, 10 | 19, 1, 16, 10 | Disputed. |
| 39-30 | Productivity / External harm affects the object | 22, 35, 13, 24 | 22, 35, 13, 14 | Disputed. |
| 39-33 | Productivity / Ease of operation | 1, 28, 7, 10 | 1, 28, 7, 19 | Disputed. |

### Order-only differences

| Cell | Parameters | CSV | 1973 table |
|------|------------|-----|------------|
| 1-27 | Weight of moving object / Reliability | 1, 3, 11, 27 | 3, 11, 1, 27 |
| 2-18 | Weight of stationary object / Illumination intensity | 19, 32, 35 | 35, 19, 32 |
| 7-3 | Volume of moving object / Length of moving object | 1, 7, 4, 35 | 1, 7, 35, 4 |
| 7-18 | Volume of moving object / Illumination intensity | 2, 13, 10 | 10, 13, 2 |
| 13-30 | Stability of the object's composition / External harm affects the object | 35, 24, 30, 18 | 35, 24, 18, 30 |
| 26-33 | Quantity of substance / Ease of operation | 35, 29, 25, 10 | 35, 29, 10, 25 |
| 34-14 | Ease of repair / Strength | 11, 1, 2, 9 | 1, 11, 2, 9 |
| 37-15 | Difficulty of detecting and measuring / Duration of action of moving object | 19, 29, 39, 25 | 19, 29, 25, 39 |
| 38-3 | Extent of automation / Length of moving object | 14, 13, 17, 28 | 14, 13, 28, 17 |
| 39-29 | Productivity / Manufacturing precision | 18, 10, 32, 1 | 32, 1, 18, 10 |

## Book check

Not started. `matrix-status.json` has `"book_verified": false` and no cell is
marked `verified`. A check against Altshuller's *40 Principles* (Shulyak and
Rodman, 1997) should start with the 29 disputed cells above.
