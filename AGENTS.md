# Instructions for Agents

These instructions apply throughout this repository, including future requests
to add batches of math competition exercises.

## Purpose and language

- Create German-language math practice booklets for children using exercises
  from different competitions.
- Write all exercise text, diagram labels, answer-sheet instructions, and
  solution explanations in natural, age-appropriate German.
- Keep repository documentation, including `README.md`, `SOURCES.md`, and this
  file, in English. Original names, source titles, and quoted exercise words
  may retain their original language when needed for attribution or analysis.

## Existing example

Before creating another batch, inspect the existing PDF and its editable data,
source notes, and generation code. Follow it as the example for layout,
formatting, illustrations, and blank/completed answer sheets:

- Reference PDF: `competitions/zrinyi/2014/grade-02/regional/mathe-knobelei-2014-klasse-2-regionalrunde.de.pdf`
- Editable content: `competitions/zrinyi/2014/grade-02/regional/exercises.de.json`
- Source and adaptation notes: `competitions/zrinyi/2014/grade-02/regional/SOURCES.md`
- PDF generation: `scripts/build_pdf.py`
- Verification: `scripts/verify_batch.py`

The reference is the **2014 Zrínyi Ilona Mathematics Competition, grade 2,
regional round (Megyei forduló)**. Use the competition, year, grade, and round
requested for each new batch; clarify missing details if they cannot be
determined from the request. Adapt page counts to the new paper's length.

## Research the exact paper

1. Search online for the original paper, all required images and diagrams,
   and the corresponding published solutions or answer key.
2. Confirm the competition, year, grade, and round. Do not mix regional,
   school, or final rounds, or use exercises from another year in a collection.
3. Include all exercises from the requested paper in their original order.
4. Record direct source URLs, relevant PDF page numbers, retrieval dates,
   publisher attribution, and illustration sources in the batch's `SOURCES.md`.
   Distinguish organizer-hosted material from third-party republications.
5. Do not invent unavailable source material or describe unverified solutions
   as official. Resolve missing or conflicting evidence before finalizing.

## German localization

- Translate all exercises from the source language into German.
- Localize all personal names, nicknames, fictional names, and geographical
  names to German names of a similar style. This includes invented landscapes
  and names inside diagrams. The exercises should read as if originally
  written for German-speaking children.
- Retain authentic competition and publisher names in source credits so the
  origin remains traceable.
- Adapt language-dependent tasks using German words, including answer options,
  encoded strings, and diagram labels. Preserve the mathematical reasoning,
  numerical result, unique correct answer, and correct answer letter.
- Explicitly verify word lengths, letter counts, shared letters, repeated
  letters, and any other linguistic constraints. Check incorrect options too
  so the adaptation does not introduce another valid answer.
- Document name mappings, word substitutions, and interpretation clarifications
  in `SOURCES.md`. Make implicit conditions explicit when necessary to preserve
  the original meaning in a standalone practice booklet.

## PDF and answer sheets

- Produce a child-friendly, printable A4 PDF following the existing booklet.
  Use readable fonts, embedded German characters, clear spacing, and diagrams
  that work in black and white.
- Include every diagram needed to solve the exercises. Use the online original
  as the reference, redraw clear vector graphics when appropriate, and preserve
  all mathematically relevant counts, shapes, orientations, and labels.
- Include a **blank Zrínyi-Kódlap-style answer sheet** for printing and filling
  in by hand. Follow the reference's numbered A–E square boxes and five-row
  blocks, with German labels and instructions. Adapt the form to the actual
  number of exercises and answer options.
- Include short German solution explanations for every exercise.
- Place a **completed Kódlap-style solution sheet at the very end of the PDF**.
  Its layout and numbering must match the blank form exactly.
- Keep source notes and solutions separate from the exercise section so the
  practice pages and blank form can be printed without revealing answers.

## Repository structure

- Give each competition, year, grade, and round its own directory under
  `competitions/`, following the existing structure.
- Use **`regional`** as the directory name for regional rounds.
- Include the generated PDF, editable exercise data, and English `SOURCES.md`
  for each batch. Keep reproducible PDF-generation code in the repository.
- The existing scripts target the first batch. Extend or parameterize them as
  needed while keeping existing booklets reproducible and preserving their files.
- Keep the English root README generic: project purpose, collection navigation,
  repository structure, and shared build or verification instructions. Do not
  add individual booklet descriptions, page breakdowns, or adaptation examples.
- Keep booklet-specific details, source links, and any batch-specific commands
  in the corresponding batch folder. Update shared README instructions only
  when the project-wide workflow changes.
- Maintain reusable agent instructions here rather than adding conversation
  transcripts or original-request sections to the README.

## Verification before completion

1. Independently solve every exercise and compare its answer with the published
   key. Confirm the localized version has the same unique correct answer.
2. Use meaningful programmatic checks for word adaptations and nontrivial
   combinatorial problems when useful; do not merely compare two copies of
   the same stored answer key.
3. Build the PDF and verify numbering, pagination, embedded fonts, text bounds,
   and the blank and completed answer forms. Check the actual drawn answer
   marks against the key.
4. Render and visually inspect every page, including diagrams, umlauts, page
   breaks, and both answer sheets.
5. Review source links and documentation for accuracy and consistency with the
   generated booklet.

Current build and verification commands, after installing `requirements.txt`
in a virtual environment and providing DejaVu Sans fonts:

```bash
.venv/bin/python scripts/build_pdf.py
.venv/bin/python scripts/verify_batch.py
```

Document the equivalent commands for any additional batch tooling.
