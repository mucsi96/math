# Math – Math Puzzles for Children

German-language practice booklets featuring exercises from different math
competitions, child-friendly illustrations, answer sheets, and solutions.
Names, places, and language-dependent puzzles are adapted for German-speaking
children while preserving mathematical results and correct answer letters.

## Browse the collection

Booklets are organized under [competitions/](competitions/) by competition,
year, grade, and round. Each batch includes:

- A printable German PDF with exercises and illustrations.
- A blank answer sheet and a completed solution sheet.
- German solution explanations and editable exercise data.
- English `SOURCES.md` documentation with source links, illustration credits,
  and localization notes.

Booklets are designed for A4 printing and handwritten answers, with embedded
fonts and illustrations suitable for black-and-white printing. Keep solution
pages separate when printing practice material.

## Build and verify

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
Both scripts accept `--batch <batch-directory>` to select a booklet; without
it they use the reference batch. The verifier also accepts
`--render-dir <directory>` to render every page for visual review.
After dependencies are installed, the build runs without network access and
writes the PDF alongside the JSON file. Output is deterministic when using
the same Python, package, and font versions.

Verification covers mathematical results, language-dependent adaptations,
pagination, embedded fonts, text boundaries, and the actual answer marks drawn
in the PDF. Generated pages should also be visually inspected. See the build
scripts and batch documentation for supported targets and any batch-specific
commands.

## Repository structure

```text
competitions/
  <competition>/
    <year>/
      grade-<NN>/
        <round>/
          exercises.de.json
          SOURCES.md
          <booklet>.de.pdf
scripts/
  build_pdf.py
  verify_batch.py
requirements.txt
```

Use `regional` for regional rounds. Keep booklet-specific details and source
notes in the corresponding batch folder. Extend the build and verification
tooling as needed for additional batches.

## Adding another batch

Agent instructions are maintained in [AGENTS.md](AGENTS.md). They cover source
research, German localization, PDF layout, answer sheets, and verification.
Specify the competition, year, grade, and round when requesting a new batch.
Follow the reference PDF identified in the agent instructions for layout and
formatting.

## Attribution

This collection contains unofficial German adaptations. Original publishers,
sources, and adaptations are documented in each batch's `SOURCES.md`. Rights
to the original competition material remain with their respective holders;
no open license is claimed for that material.
