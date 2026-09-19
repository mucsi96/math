# Sources and Adaptation Notes

## Identification

- **Competition:** Zrínyi Ilona Matematikaverseny, 2014.
- **Grade:** 2 (original label: “2. osztály”).
- **Round:** **Megyei forduló** (regional round), labeled “Regionalrunde” in the German booklet.
- **Scope:** all 25 exercises from this round, in their original order.
- **Original publisher:** MATEGYE Alapítvány, Kecskemét, 2014.
- **Compiled by, according to the cover:** Székeli Andrea.
- **Sources accessed:** September 19, 2026.

## Original exercises and illustrations

The [Matek Kicsiknek collection](https://matekkicsiknek.webnode.hu/zrinyi/)
links to the [original scanned PDF](https://fe2d198f3f.clvaw-cdnwnd.com/f4c1eb687f8ffbeb900731e24605c892/200000082-640486404a/Zr%C3%ADnyi%20Ilona%20matekverseny%202%20oszt%C3%A1ly%202014-2018%20%282%29.pdf?ph=fe2d198f3f)
under **2014 / 2. osztály megyei 2014–2018** (grade 2, regional rounds, 2014–2018).

The file contains 12 PDF pages covering several years. **Only the first two
PDF pages belong to the 2014 paper used here:**

- PDF page 1: exercises 20–25 on the left; cover with the year, round, and grade on the right.
- PDF page 2: exercises 1–11 on the left; exercises 12–19 on the right.

SHA-256 of the downloaded original file:

```text
5f831b37d9210ad5931dd67028b5227e14bb12295f2c6ffbb348127cd3be23a8
```

Illustrations for exercises **1, 3, 7, 9, and 11** were redrawn as scalable
vector graphics using this scan as a reference. Exercise **14** contains a
newly typeset, translated table. All mathematically relevant features are
preserved: four rotated hippos and a lion at position D; two identical faces;
six triangles and five circles; a 4×4 grid; shapes with 3/4/3/4 sides and the
numbers 2/0/1/4 inside; and unchanged positions of the nine timetable entries.
The drawing code is in
[`scripts/build_pdf.py`](../../../../../scripts/build_pdf.py).

## Answer key

Two accessible online sources reproduce the same published answer key:

1. [Matek Kicsiknek, 2014 section, grade 2](https://matekkicsiknek.webnode.hu/zrinyi/).
2. [“Zrínyi MEGOLDÓKULCS 2014” (answer key), text preview](https://pdfcoffee.com/zrinyi-megoldokulcs-2014-pdf-free.html),
   explicitly labeled “Megyei forduló / 2. évfolyam” (regional round / grade 2).

```text
Exercises  1– 5: DCBCD
Exercises  6–10: EBBEC
Exercises 11–15: BDCBC
Exercises 16–20: DCDBD
Exercises 21–25: ABCEB
```

These are republications, rather than an answer key retrieved directly from
the organizer. All 25 solutions were also independently checked through
calculation or logical reasoning. The German solution explanations were
written specifically for this booklet.

## Blank and completed Kódlap-style answer sheets

Template: [official sample Kódlap from MATEGYE Alapítvány](http://www.mategye.hu/download/zrinyi/minta_kodlap.pdf).
At the time of retrieval, the server was accessible over HTTP but not HTTPS.

The adapted layout places exercises 1–15 on the left and 16–25 on the right,
in groups of five with A–E columns and square checkboxes. The template also
includes exercises 26–30; these are omitted for this 25-exercise paper. Labels
and instructions are in German. The blank sheet appears on page 7, and the
same form with the correct answers marked appears on the final page (11).
The forms are intended for printing and handwritten answers.

## Localization

| Original | German adaptation | Exercise |
|---|---|---|
| Kecskemét / KECSKEMÉT | Kalkar / KALKAR | 2, 21 |
| Bazsi | Ben | 4 |
| Sári | Sarah | 8 |
| Picúr | Felix | 9 |
| Hófehérke, Hapci | Schneewittchen, Zwerg Niesbert | 10 |
| Csiribiri tanár úr | Meister Hokuspokus | 14 |
| Tudorka | Professor Pfiffig | 15 |
| Tomi, Karcsi | Tom, Karl | 16 |
| Zsuzsi, Kati | Susanne, Katharina | 19 |
| Veszprém, Székesfehérvár | Bremen, Hannover | 21 |
| Bambi, Dumbo | Reh Fritzi, Elefant Oskar | 22 |
| Nekeresd-erdő, Seholsincs-hegy | Zauberwald, Wolkenberg | 22 |
| Anna | Anna (also a common German name) | 23 |
| Misi, Flóri | Michael, Florian | 24 |

The competition is called “Mathe-Knobelwettbewerb” in the exercise text.
The authentic Hungarian competition and publisher names are retained only
in source credits so the material's origin remains traceable.

### Language-dependent exercises

- **2:** KECSKEMÉT and KALKAR each contain exactly two Ks; answer **C**.
- **15:** LAP → TAL. The middle letter remains A. Inserting an extra A after
  every typed letter produces **TAAALA**, still answer **C**. All five answer
  options were consistently adapted by mapping L → T and P → L while keeping
  A unchanged.
- **24:** **BLUME and KREIS** replace MÉZES and MÁLNA. All answer options
  are replaced with German words. Every word used has five distinct letters,
  making the counting rule unambiguous without special rules for repeated
  letters.

| Answer | Word | Letters shared with BLUME | Letters shared with KREIS |
|---|---|---:|---:|
| A | LAMPE | 3 | 1 |
| B | TIGER | 1 | 3 |
| C | MULDE | 4 | 1 |
| D | STUHL | 2 | 1 |
| **E** | **WOLKE** | **2 (L, E)** | **2 (K, E)** |

Both clues (“2”), the type of puzzle, and the unique correct answer **E**
are preserved. The incorrect words and their respective overlap counts
were newly chosen.

### Important interpretation details

- **21:** The regional round takes place before the final. “So far” therefore
  covers only 24 completed competition years: **24 − 2 − 2 − 1 = 19**,
  answer **A**. This timing, implicit in the original, is stated explicitly
  so the practice version remains unambiguous whenever it is used.
- **25:** “Next to every chair” applies **to empty chairs too**. Applying the
  rule only to occupied chairs would change the problem. Under the full
  rule, at most **6** seats can be occupied, giving answer **B**. The
  verification script checks all 2¹⁴ possible seating arrangements.

This adaptation is unofficial. Rights to the original exercises remain with
their respective holders; this collection does not claim an open license
for third-party source material.
