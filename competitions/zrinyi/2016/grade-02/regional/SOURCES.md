# Sources and Adaptation Notes

## Identification

- Competition: **Zrínyi Ilona Matematikaverseny 2016**.
- Grade: **2. osztály** (grade 2).
- Round: **megyei forduló** (regional round).
- Scope: all 25 exercises, in their original order.
- Original publisher: **MATEGYE Alapítvány**, Kecskemét, 2016.
- Compiler credited on the cover: **Székeli Andrea**.
- Sources retrieved: **November 11, 2026**.

## Original paper and illustrations

The third-party [Matek a neten 2016 collection](http://www.matekaneten.hu/2016.html)
links its “2. osztály” entry to this [two-page scanned paper](https://drive.google.com/file/d/1ehlQ4k-eVMgsatDDHDK8MWXRGN979ufo/view?usp=sharing).
The [direct download](https://drive.google.com/uc?export=download&id=1ehlQ4k-eVMgsatDDHDK8MWXRGN979ufo)
was retrieved and visually read. This is a third-party republication, not an
organizer-hosted download.

- PDF page 1: exercises 20–25 on the left; identifying cover on the right.
- PDF page 2: exercises 1–11 on the left; exercises 12–19 on the right.
- The cover explicitly confirms year, grade, round, and publisher.
- SHA-256: `63bd209b8e344a8399705fe2353d382e4232b0946c267454d24d4c39ef051898`.

The older collection URL listed in the reference batch,
`https://matekkicsiknek.webnode.hu/zrinyi/`, returned HTTP 410, and its linked
2014–2018 scan returned HTTP 403. Neither was used as the content source for
this booklet.

All required diagrams are vector redraws based on the retrieved paper;
no generated or stock illustrations are used. Drawing code:
[`scripts/diagrams_2016.py`](../../../../../scripts/diagrams_2016.py).

| Exercise | Source page | Preserved visual information |
|---|---:|---|
| 1 | 2 | Rectangle, circle, semicircle, triangle, cross, in A–E order |
| 2 | 2 | Completed short-haired face; A has ears, eyes/nose and smile; B has additional long hair; C outline only; D eyes/nose and smile; E eyes/nose only |
| 3 | 2 | Digital display 10:52, included directly in the German question |
| 9 | 2 | Bottle/bread/apple counts A 2/2/3, B 2/1/2, C 2/2/1, D 3/1/1, E 3/1/2 |
| 12 | 2 | Folded quarter-circle with a dashed cut across its central corner; options show one slit, crossed slits, one triangular hole, square hole, two opposite triangular holes |
| 16 | 2 | Domino top/bottom counts 3/6, 4/5, 1/4, 3/5, 6/1 |
| 18 | 2 | Top-middle arrow points down; bottom arrows point to the two outer top circles |
| 21 | 1 | Two-column, three-row grid, start bottom-left and finish top-right |
| 22 | 1 | Marked positions separated by 11 and 3 units; labels ♣♥, ☺♣, ♦■ |
| 24 | 1 | Same five four-vertex graphs and all original edges |

The orientation of the quarter-circle, the arrow directions, number-line
spacing, and graph edges were checked against the scan. Decorative drawing
details are simplified while retaining the information needed to solve each
problem.

## Published answer key

[Zrínyi – Gordiusz matematikaverseny 2016, Megoldókulcs](https://kop.at.ua/kmpsz16/zrinyi2016_megold.pdf),
PDF page 1, explicitly labels the row **Megyei forduló / 2. évfolyam**:

```text
 1– 5  DBECC
 6–10  EEDEB
11–15  EDEBA
16–20  DDCBE
21–25  DDADE
```

SHA-256: `fe603f37334db365b0c357921ff5b4857147c22581e59e041de23094b1ffcc36`.
This is a third-party copy of the published key, not a key retrieved directly
from the organizer. All answers were independently solved and compared with
this row. German solution explanations are original to this adaptation.

## Localization and interpretation

| Original | German | Exercises |
|---|---|---|
| Bolka, Lolka | Ben, Leo | 2 |
| Ági | Anna | 3 |
| Minyon | Minion (usual German spelling) | 4 |
| Peti | Peter | 6, 8, 17 |
| Piroska | Rotkäppchen | 9 |
| Tibi | Tim | 10 |
| VIOLA | VIOLA (also a German given name) | 11 |
| Kati | Katharina | 13 |
| Balázs | Ben | 19 |
| Bori | Britta | 20 |
| Csiga Csilla | Schnecke Susi | 21 |
| Csi, Csú | Schneckendorf, Schneckenberg | 21 |
| Dodó | Daniel | 22 |
| bergengóc language | Sprache der Bergwichtel | 24 |
| Gombóc Artúr | Arthur Knödel | 25 |

- **8:** Forints become cents, preserving the unit price 15, quantity 3,
  numerical answer 45, and all five options. This is localization, not a
  currency conversion.
- **11:** VIOLA contains five distinct letters. The four possible adjacent
  swaps are IVOLA, VOILA, VILOA, VIOAL. Of the original options OLIVA, VLIOA,
  LIOVA, AIOVL, VIOAL, only E is in that set. All options retain exactly the
  original five letters. No word substitution is needed.
- **12:** The second fold is explicitly described as producing a quarter-circle,
  as shown in the original. Both sides of the paper remain gray.
- **16:** “Turn over” explicitly means exchanging the top and bottom halves.
- **21:** Movement is along grid edges, only up or right; start and finish are
  labeled with the localized place names.
- **22:** All five symbols denote distinct digits, as in the source. Exhausting
  digit assignments gives only 76, 87, 90, so the face denotes 8.
- **23:** The one-way first trip and strictly later exit are made explicit.
  There are six ordered boarding/exit pairs, not twelve bidirectional pairs.
- **24:** “Connected exactly when” clarifies that every shared letter requires
  an edge. Repeated letters within a word do not change the result. D is
  impossible because a two-letter center cannot meet three pairwise disjoint
  leaf words. Witness words for the other graphs (top, left, right, bottom):
  A: AB/AC/BD/EF; B: AB/AC/BD/CD; C: DE/AB/AC/BC; E: AB/AC/DE/BD.
  These are verification examples, not extra words on the practice page.
- **25:** The two compound claims mean both named hats have pompoms. The four
  truth values are false, false, true, false in every permitted arrangement.

## Answer sheets, layout, and verification

The organizer-hosted [sample Kódlap](http://www.mategye.hu/download/zrinyi/minta_kodlap.pdf)
was retrieved over HTTP. The shared renderer follows the reference booklet:
five-row A–E square-box blocks, tasks 1–15 left and 16–25 right.
German labels and handwriting instructions replace the original labels.

The booklet has **11 A4 pages**:

- 1–6: exercises (1–4, 5–9, 10–13, 14–18, 19–22, 23–25).
- 7: blank answer sheet; print pages **1–7** for practice.
- 8: source credits and adaptation notes.
- 9–10: German solution explanations.
- 11: completed answer sheet, at the very end.

From the repository root, with dependencies installed:

```bash
.venv/bin/python scripts/build_pdf.py --batch competitions/zrinyi/2016/grade-02/regional
.venv/bin/python scripts/verify_batch.py --batch competitions/zrinyi/2016/grade-02/regional --render-dir /tmp/opencode/2016-render
```

[`scripts/verify_2016.py`](../../../../../scripts/verify_2016.py) independently
checks the arithmetic, pencil constraints, all adjacent-letter swaps and
distractors, domino flips, all 24 arrow assignments, digit occurrences,
monotone grid walks, distinct-digit number-line assignments, bus pairs,
word-graph realizability, and all hat arrangements. Picture geometry and
folding were also reviewed visually against the scan.

The shared verifier passed numbering, page placement, A4 dimensions, embedded
DejaVu fonts, text bounds, 125 blank boxes, and the actual drawn answer crosses
decoded from the final PDF. Every rendered page was visually inspected,
including German characters, diagrams, page breaks, and both forms.

This is an unofficial adaptation. Rights to the original competition material
remain with their respective holders; no open license is claimed for it.
