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
- [Sources, illustration credits, and localization notes (in German)](competitions/zrinyi/2014/grade-02/regional/SOURCES.md)

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

## Reusable prompt for the next batch

Replace the placeholders before use. This prompt includes the follow-up
requirements specifying the round and both Kódlap-style answer sheets.

```text
Add a new batch to the existing math repository containing German-language
math competition exercises for children.

Competition: [COMPETITION]
Year: [YEAR]
Grade: [GRADE]
Round: [ROUND — e.g. Megyei forduló / regional round]
Original language: [LANGUAGE — e.g. Hungarian]

1. Search online for the exact original paper, its exercise images/diagrams,
   and the corresponding published solutions or answer key. Verify the year,
   grade, and round. Include all exercises from that paper in original order.
   Record direct source URLs, page references, and the retrieval date.
2. Create a printable, child-friendly German PDF. Translate all exercises
   from the original language into natural, age-appropriate German.
3. Localize ALL personal names, nicknames, fictional names, and geographical
   names to German names of a similar style. The exercises should read as if
   originally written for German-speaking children. Keep authentic source
   names in the source credits so the origin remains traceable.
4. Adapt language-dependent exercises using German words, including answer
   options, encoded strings, and diagram labels. Preserve the mathematical
   reasoning, numerical result, unique correct answer, and correct answer
   letter. Verify letter counts, word lengths, shared letters, and any other
   language-dependent constraints. Document each adaptation.
5. Include every necessary diagram, using the online originals as references.
   Recreate clear printable graphics when appropriate and record their sources.
6. Include a BLANK Zrínyi-Kódlap-style answer sheet to fill in, with numbered
   exercises and A–E boxes grouped like the official form. Adapt the form to
   the actual number of exercises and use German labels and instructions.
7. Include short German explanations of the solutions and a COMPLETED
   Zrínyi-Kódlap-style solution sheet at the END of the PDF. The blank and
   completed forms must have matching numbering and layout.
8. Independently solve every exercise and compare with the published key.
   Check that the German adaptations preserve the correct answer. Resolve
   ambiguities explicitly and document any clarifications. Do not invent
   unavailable source material or present unverified answers as official.
9. Keep editable exercise data and reproducible PDF-generation code in the
   repository. Render and visually inspect the PDF, including diagrams,
   page breaks, umlauts, the blank form, and the completed answer marks.
10. Keep the README entirely in English. Update its catalog with the new PDF
    and source notes, and retain this reusable prompt for future batches.
    Use regional as the folder name for regional rounds.

For the first batch these settings were:
Zrínyi Ilona Matematikaverseny / 2014 / grade 2 / Megyei forduló / Hungarian.
```

### Original request (verbatim)

> create a new github repo called math and clone it to math project. This repo should hold math exercises from different math competitions in german for kids. As first batch please add a german PDF based on 2014 Zrínyi Ilona Matematikaverseny for 2.rd class kids (do online search for images and solutions) including a solution sheet on the end. You have to translate from hungarian to german. But important. You must traslate all hungarian names including geographic names to similar style german. So all exercises should look like originally created for german kids. Also hungarian exercises based on words should be adjusted to use german words instead. But important that translation and any language based adjustment should keep the correct solution intact. Lastly add this propts to reamde itself so we can reuse it for next batch.

Follow-up requirements (verbatim):

> I forgot to say "Megyei fordulo"

> I forgot to say that the solution sheet should like Zrinyi Kodlap

> Please Actualy add to the PDF a Zrinyi empty kodalp as well to fill in

> can we avoid using county please? It's way  to close to country.

> Also reamede must be fully in english

## Attribution

This collection contains unofficial German adaptations. The first original
paper was published by **MATEGYE Alapítvány**. Sources and adaptations are
documented for each booklet; no open license is claimed for the original
competition material.
