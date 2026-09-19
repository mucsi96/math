# Math – Mathe-Knobeleien für Kinder

Deutschsprachige Übungshefte mit Aufgaben aus verschiedenen
Mathematikwettbewerben, kindgerechten Illustrationen, Antwortbögen und
Lösungen. Namen, Orte und sprachabhängige Rätsel werden für deutschsprachige
Kinder angepasst; mathematische Ergebnisse und richtige Antwortbuchstaben
bleiben erhalten.

## Erstes Heft: Regionalrunde 2014, Klasse 2

**[PDF öffnen / herunterladen](competitions/zrinyi/2014/grade-02/county/mathe-knobelei-2014-klasse-2-regionalrunde.de.pdf)**

Grundlage: **Zrínyi Ilona Matematikaverseny 2014 – Megyei forduló – 2. osztály**.
Das Heft enthält alle **25 Aufgaben** dieser Runde in derselben Reihenfolge.

| Seiten | Inhalt |
|---|---|
| 1–6 | Deutsche Aufgaben mit neu gezeichneten Abbildungen und übersetztem Stundenplan |
| 7 | **Leerer Antwortbogen im Zrínyi-Kódlap-Stil** zum Ausfüllen |
| 8 | Quellen und Hinweise für Erwachsene |
| 9–10 | Kurze deutsche Lösungswege zu allen 25 Aufgaben |
| 11 | **Ausgefüllter Lösungsbogen im Zrínyi-Kódlap-Stil**, ganz am Ende |

Die Antwortbögen haben die A–E-Kästchen und Fünferblöcke der offiziellen
Vorlage: Aufgaben 1–15 links und 16–25 rechts. Sie sind für den Ausdruck auf
**A4** und das handschriftliche Ausfüllen vorgesehen. Zum Üben die Seiten
1–7 ausdrucken; die Lösungsseiten getrennt aufbewahren. Die Schriften sind
eingebettet, die Abbildungen sind skalierbar und schwarz-weiß druckbar.

- [Bearbeitbare Aufgaben und Lösungen (JSON)](competitions/zrinyi/2014/grade-02/county/exercises.de.json)
- [Quellen, Bildnachweise und Lokalisierungsprotokoll](competitions/zrinyi/2014/grade-02/county/SOURCES.md)

### Geprüfte Anpassungen

- **Ortsnamen:** unter anderem Kecskemét → Kalkar, Veszprém → Bremen und
  Székesfehérvár → Hannover; auch die erfundenen Landschaftsnamen sind deutsch.
- **Aufgabe 2:** KALKAR enthält wie der Originalname zwei K.
- **Aufgabe 15:** Das deutsche Wort TAL bewahrt die Einfüge-Regel; die Ausgabe
  lautet TAAALA, Antwort C.
- **Aufgabe 24:** BLUME und KREIS mit fünf deutschen Antwortwörtern; nur WOLKE
  teilt mit beiden Wörtern jeweils zwei Buchstaben, Antwort E.
- **Aufgaben 21 und 25:** Der Zeitpunkt vor dem diesjährigen Finale sowie die
  Nachbarregel auch für freie Stühle sind ausdrücklich formuliert.

Alle 25 Antwortbuchstaben stimmen mit dem in zwei Onlinequellen
wiedergegebenen Schlüssel überein. Die Lösungen sind zusätzlich unabhängig
nachgerechnet; für die Kinoaufgabe werden alle 16.384 Belegungen geprüft.

## PDF selbst erzeugen

Voraussetzungen: Python **3.10+**, `venv` und die Schrift **DejaVu Sans**
(unter Debian/Ubuntu Paket `fonts-dejavu-core`).

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_pdf.py
.venv/bin/python scripts/verify_batch.py
```

Bei einem anderen Schriftverzeichnis:

```bash
.venv/bin/python scripts/build_pdf.py --font-dir /pfad/zu/dejavu
```

Das Verzeichnis muss `DejaVuSans.ttf` und `DejaVuSans-Bold.ttf` enthalten.
Der Build benötigt nach der Installation keinen Netzwerkzugriff und schreibt
die PDF direkt neben die JSON-Datei. Er ist bei gleicher Python-, Paket- und
Schriftversion deterministisch.

Die Prüfung kontrolliert mathematische Ergebnisse, deutsche Buchstabenrätsel,
Seitenaufteilung, eingebettete Schriften und Textränder. Außerdem liest sie die
**tatsächlich gezeichneten Kästchen und Kreuze aus der PDF** aus: 125 leere
Kästchen auf dem Übungsbogen und genau 25 richtige Kreuze auf dem Lösungsbogen.
Bei der Ersterstellung wurden alle PDF-Seiten zusätzlich visuell geprüft.

## Struktur für weitere Hefte

```text
competitions/
  zrinyi/
    2014/
      grade-02/
        county/
          exercises.de.json
          SOURCES.md
          mathe-knobelei-2014-klasse-2-regionalrunde.de.pdf
scripts/
  build_pdf.py
  verify_batch.py
requirements.txt
```

Weitere Wettbewerbe, Jahre, Klassen und Runden bekommen eigene Unterordner.
Die beiden vorhandenen Skripte sind auf das erste Heft zugeschnitten; für neue
Hefte werden Inhalt, Ausgabeziel und fachliche Prüfungen passend erweitert.

## Wiederverwendbarer Auftrag für das nächste Heft

Die Platzhalter vor der Verwendung ersetzen. Der folgende Auftrag enthält
auch die nachträglichen Präzisierungen zur Runde und zu den beiden Kódlap-Bögen.

```text
Add a new batch to the existing math repository containing German-language
math competition exercises for children.

Competition: [COMPETITION]
Year: [YEAR]
Grade: [GRADE]
Round: [ROUND — e.g. Megyei forduló / county round]
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
10. Update the README catalog with the new PDF and source notes, and retain
    this reusable prompt for future batches.

For the first batch these settings were:
Zrínyi Ilona Matematikaverseny / 2014 / grade 2 / Megyei forduló / Hungarian.
```

### Ursprünglicher Auftrag (unverändert)

> create a new github repo called math and clone it to math project. This repo should hold math exercises from different math competitions in german for kids. As first batch please add a german PDF based on 2014 Zrínyi Ilona Matematikaverseny for 2.rd class kids (do online search for images and solutions) including a solution sheet on the end. You have to translate from hungarian to german. But important. You must traslate all hungarian names including geographic names to similar style german. So all exercises should look like originally created for german kids. Also hungarian exercises based on words should be adjusted to use german words instead. But important that translation and any language based adjustment should keep the correct solution intact. Lastly add this propts to reamde itself so we can reuse it for next batch.

Nachträgliche Ergänzungen (unverändert):

> I forgot to say "Megyei fordulo"

> I forgot to say that the solution sheet should like Zrinyi Kodlap

> Please Actualy add to the PDF a Zrinyi empty kodalp as well to fill in

## Herkunft

Die Sammlung enthält inoffizielle deutsche Bearbeitungen. Die erste Vorlage
stammt von der **MATEGYE Alapítvány**. Quellen und Veränderungen sind pro Heft
dokumentiert; für die Originalaufgaben wird keine freie Lizenz behauptet.
