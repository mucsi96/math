# Math – Math Puzzles for Children

German-language practice booklets featuring exercises from different math
competitions, child-friendly illustrations, answer sheets, and solutions.
Names, places, and language-dependent puzzles are adapted for German-speaking
children while preserving mathematical results and correct answer letters.

## First booklet: 2014 regional round, grade 2

**[Open / download the PDF](competitions/zrinyi/2014/grade-02/regional/mathe-knobelei-2014-klasse-2-regionalrunde.de.pdf)**

Based on the **2014 Zrínyi Ilona Mathematics Competition – regional round
(Megyei forduló) – grade 2**. The booklet includes all **25 exercises** from
this round in their original order.

| Pages | Contents |
|---|---|
| 1–6 | German exercises with redrawn diagrams and a translated timetable |
| 7 | **Blank Zrínyi-Kódlap-style answer sheet** to fill in |
| 8 | Sources and notes for adults |
| 9–10 | Short German solution explanations for all 25 exercises |
| 11 | **Completed Zrínyi-Kódlap-style solution sheet**, at the very end |

The answer sheets follow the official template's A–E boxes and groups of five:
exercises 1–15 on the left and 16–25 on the right. They are designed for
**A4 printing** and handwritten answers. Print pages 1–7 for practice and keep
the solutions separate. Fonts are embedded, and illustrations are scalable
and suitable for black-and-white printing.

- [Editable exercises and solutions (German JSON)](competitions/zrinyi/2014/grade-02/regional/exercises.de.json)
- [Sources, illustration credits, and localization notes](competitions/zrinyi/2014/grade-02/regional/SOURCES.md)

### Verified adaptations

- **Place names:** examples include Kecskemét → Kalkar, Veszprém → Bremen,
  and Székesfehérvár → Hannover. Fictional geographical names are also German.
- **Exercise 2:** KALKAR contains two Ks, just like the original place name.
- **Exercise 15:** The German word TAL preserves the letter-insertion rule;
  the output is TAAALA, answer C.
- **Exercise 24:** BLUME and KREIS are paired with five German answer words.
  Only WOLKE shares exactly two letters with each clue word, giving answer E.
- **Exercises 21 and 25:** The timing before this year's final and the
  neighboring-seat rule applying to empty seats are stated explicitly.

All 25 answer letters match the published key reproduced by two online
sources. Solutions have also been independently checked; the cinema seating
problem is verified by examining all 16,384 possible arrangements.

## Build the PDF

Requirements: Python **3.10+**, `venv`, and the **DejaVu Sans** font
(`fonts-dejavu-core` on Debian/Ubuntu).

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_pdf.py
.venv/bin/python scripts/verify_batch.py
```

To use a different font directory:

```bash
.venv/bin/python scripts/build_pdf.py --font-dir /path/to/dejavu
```

The directory must contain `DejaVuSans.ttf` and `DejaVuSans-Bold.ttf`.
After dependencies are installed, the build runs without network access and
writes the PDF alongside the JSON file. Output is deterministic when using
the same Python, package, and font versions.

Verification checks mathematical results, German letter puzzles, pagination,
embedded fonts, and text boundaries. It also reads the **actual boxes and
crosses drawn in the PDF**: 125 empty boxes on the practice answer sheet and
exactly 25 correct crosses on the solution sheet. Every PDF page was also
visually inspected when the booklet was first created.

## Structure for future booklets

```text
competitions/
  zrinyi/
    2014/
      grade-02/
        regional/
          exercises.de.json
          SOURCES.md
          mathe-knobelei-2014-klasse-2-regionalrunde.de.pdf
scripts/
  build_pdf.py
  verify_batch.py
requirements.txt
```

Additional competitions, years, grades, and rounds get their own subfolders.
Use `regional` for regional rounds. The two existing scripts are tailored to
the first booklet; extend their content, output paths, and mathematical checks
as needed for future batches.

## Adding another batch

Agent instructions are maintained in [AGENTS.md](AGENTS.md). They cover source
research, German localization, PDF layout, answer sheets, and verification.
Specify the competition, year, grade, and round when requesting a new batch.
The existing booklet serves as the layout and formatting example.

## Attribution

This collection contains unofficial German adaptations. The first original
paper was published by **MATEGYE Alapítvány**. Sources and adaptations are
documented for each booklet; no open license is claimed for the original
competition material.
