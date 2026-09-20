# Sources and Adaptation Notes

## Identification and retrieval

- **Competition:** 2015 Zrínyi Ilona Matematikaverseny.
- **Grade and round:** 2. osztály, megyei forduló (grade 2, regional round).
- **Scope:** all 25 exercises, in original order.
- **Publisher:** MATEGYE Alapítvány, Kecskemét, 2015.
- **Compiler credited on the cover:** Székeli Andrea.
- **Retrieval date:** September 20, 2026.

The [Matek Kicsiknek archive](https://matekkicsiknek.webnode.hu/zrinyi/)
links to the [two-page original scan](https://fe2d198f3f.clvaw-cdnwnd.com/f4c1eb687f8ffbeb900731e24605c892/200000080-4e2bd4e2bf/Zrinyi%202015%20megyei%202o.pdf?ph=fe2d198f3f)
in its **2015 / 2. osztály megyei** section. This is a third-party
republication, not an organizer-hosted download. The original cover confirms
the year, grade, round, publisher, and compiler.

- PDF page 1: exercises 20–25 on the left, original cover on the right.
- PDF page 2: exercises 1–11 on the left, 12–19 on the right.
- Download SHA-256: `c066eccff0dd0aec53b413fd02adc93ff8b4138c9db6edb7db263527087997dc`.

## Published answer key and independent solutions

The same archive's 2015 section explicitly labels its grade-2 regional key
“2. osztály megyei megoldókulcs”:

```text
 1– 5: EBDDD
 6–10: DEDCE
11–15: EBACA
16–20: BBECE
21–25: CCCED
```

This key was retrieved from the third-party archive, not directly from the
organizer. Every exercise was independently solved and agrees with it.
The German explanations are newly written, not official published solutions.
`scripts/verify_2015.py` checks arithmetic, every letter-puzzle alternative,
coin counts and totals, car pairs, both-even-digit numbers, all seating
assignments, flower inventories and bouquet feasibility, and ball-color bounds.
The three purely visual choices (1, 4, 6) were checked against the scan.

## Illustrations

All six illustrated tasks are newly drawn black-and-white vector graphics
in [`scripts/diagrams_2015.py`](../../../../../scripts/diagrams_2015.py),
referencing the original scan, not external clip art:

| Exercise | Source page | Features preserved |
|---|---|---|
| 1 | 2, left | Five pencils; length order E < B < A < C < D; common baseline. |
| 4 | 2, left | Circular heads; star, rectangular, square, circular, triangular eyes in A–E order; nose directions right/left/left/right/left. |
| 6 | 2, left | Two equal square pieces; edge-sharing, rotated corner-sharing, diagonal corner-sharing, two triangles, and square plus rotated square in A–E order. |
| 8 | 2, left | Two rows of six plants; flowers at top positions 1/3/5 and bottom positions 1/4/5/6. |
| 12 | 2, right | All five purses and all coin values and positions: A 50/20/20 above 10/20; B 20/20 above 20/20/20; C 50/20 above 10/10; D 20/20 above 10/20/10; E 20/10/20 above 20/20/10. |
| 20 | 1, left | Initial cat–mouse–dog order; all five alternative orders unchanged; dog tallest, mouse smallest. |

## Localization and explicit assumptions

| Original | German adaptation | Exercise |
|---|---|---|
| Garfield | Kater Kasimir | 4 |
| Anna | Anna (also a German name) | 5, 22 |
| Erzsi néni | Frau Elsa | 8 |
| Béci | Ben | 9 |
| TÓBIÁS | TOBIAS | 10 |
| Marika | Marie | 12 |
| Feri | Felix | 13 |
| Samu, Zoli | Samuel, Simon | 14 |
| Réka | Rebecca | 15 |
| Nyakigláb, Málészáj | Lulatsch, Trödelfritz | 16 |
| Marci | Martin | 18 |
| Baltazár | Balthasar | 19 |
| Tomi | Tom | 21 |
| Bálint, Csilla, Dávid | Benjamin, Clara, David | 22 |
| Vera | Vera (also a German name) | 24 |

- **9 and 12:** Forints become cents with all numeric values unchanged.
  All illustrated denominations (10, 20, 50) are valid euro-cent coins.
- **10:** TÓBIÁS → TOBIAS preserves six distinct letters. Removing positions
  2/4/6 leaves positions 1/3/5, TBÁ → TBA. All options are adapted by the
  same accent removal: TBS, TOI, BIA, OBI, TBA. Only E is correct.
- **6:** Rotation is explicitly allowed; cutting and overlapping are not.
  This makes the original square-piece interpretation explicit.
- **17:** All non-end seats are explicitly occupied by children, as intended
  in the school-outing problem; 77 seats minus 10 adults gives 67 children.
- **20:** The second movement is explicitly a dog–cat swap, retaining the
  other animal's position and the intended E answer.
- **22:** Girls and boys are explicitly identified so the reasoning does not
  depend on familiarity with Hungarian names. Each child uses a different
  piece of furniture, including just one child on the bench.

## Answer sheets, pagination, and verification

The [organizer-hosted sample Kódlap](http://www.mategye.hu/download/zrinyi/minta_kodlap.pdf)
(PDF page 1; retrieved over HTTP) supplies the numbered A–E square boxes
in five-row blocks. The booklet reuses the reference batch's form layout,
adapted to 25 questions: 1–15 on the left, 16–25 on the right.

The booklet has **12 A4 pages**: exercises on pages 1–7, blank form on page 8,
source notes on page 9, explanations on pages 10–11, completed form on page 12.
Print pages **1–8** for practice without revealing solutions.

From the repository root, after installing the shared dependencies and fonts:

```bash
.venv/bin/python scripts/build_pdf.py --batch competitions/zrinyi/2015/grade-02/regional
.venv/bin/python scripts/verify_batch.py --batch competitions/zrinyi/2015/grade-02/regional --render-dir /tmp/opencode/math-2015-review
```

The verifier checks numbering, planned page groups, A4 dimensions, embedded
fonts, text bounds, 125 empty answer boxes, and the 25 actual drawn crosses
decoded from the final PDF. Every rendered page is also visually reviewed.
The original 2014 batch remains reproducible with the no-argument commands.

This is an unofficial adaptation. Rights to the original tasks and artwork
remain with their respective holders; no open license is claimed for them.
