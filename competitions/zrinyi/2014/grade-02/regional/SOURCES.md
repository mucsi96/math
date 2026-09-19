# Quellen und Bearbeitungsprotokoll

## Identifikation

- **Wettbewerb:** Zrínyi Ilona Matematikaverseny, 2014.
- **Klassenstufe:** 2. osztály (2. Klasse).
- **Runde:** **Megyei forduló**, hier als „Regionalrunde“ bezeichnet.
- **Umfang:** alle 25 Aufgaben dieser Runde, in Originalreihenfolge.
- **Originalherausgeber:** MATEGYE Alapítvány, Kecskemét, 2014.
- **Zusammenstellung laut Titelblatt:** Székeli Andrea.
- **Quellen abgerufen:** 19. September 2026.

## Originalaufgaben und Bilder

Die [Sammlung „Matek Kicsiknek“](https://matekkicsiknek.webnode.hu/zrinyi/)
verlinkt unter **2014 / 2. osztály megyei 2014–2018** den
[Originalscan als PDF](https://fe2d198f3f.clvaw-cdnwnd.com/f4c1eb687f8ffbeb900731e24605c892/200000082-640486404a/Zr%C3%ADnyi%20Ilona%20matekverseny%202%20oszt%C3%A1ly%202014-2018%20%282%29.pdf?ph=fe2d198f3f).

Die Datei umfasst 12 PDF-Seiten mit mehreren Jahrgängen. **Nur die ersten
beiden PDF-Seiten gehören zur hier verwendeten Ausgabe 2014:**

- PDF-Seite 1: links Aufgaben 20–25, rechts Titelblatt mit Jahr, Runde und Klasse.
- PDF-Seite 2: links Aufgaben 1–11, rechts Aufgaben 12–19.

SHA-256 der abgerufenen Originaldatei:

```text
5f831b37d9210ad5931dd67028b5227e14bb12295f2c6ffbb348127cd3be23a8
```

Die Bilder zu Aufgaben **1, 3, 7, 9 und 11** wurden anhand dieses Scans als
skalierbare Vektorgrafiken neu gezeichnet. Aufgabe **14** enthält eine neu
gesetzte, übersetzte Tabelle. Die mathematisch relevanten Merkmale bleiben
erhalten: vier gedrehte Nilpferde und ein Löwe an Position D; zwei gleiche
Gesichter; sechs Dreiecke und fünf Kreise; ein 4×4-Raster; Figuren mit den
Seitenzahlen 3/4/3/4 und den eingetragenen Zahlen 2/0/1/4; unveränderte
Positionen der neun Stundenplanfächer. Der Zeichen-Code steht in
[`scripts/build_pdf.py`](../../../../../scripts/build_pdf.py).

## Antwortschlüssel

Der veröffentlichte Schlüssel wird in zwei online zugänglichen Quellen
übereinstimmend wiedergegeben:

1. [Matek Kicsiknek, Abschnitt 2014, 2. Klasse](https://matekkicsiknek.webnode.hu/zrinyi/).
2. [„Zrínyi MEGOLDÓKULCS 2014“, Textvorschau](https://pdfcoffee.com/zrinyi-megoldokulcs-2014-pdf-free.html),
   ausdrücklich beschriftet mit „Megyei forduló / 2. évfolyam“.

```text
Aufgaben  1– 5: DCBCD
Aufgaben  6–10: EBBEC
Aufgaben 11–15: BDCBC
Aufgaben 16–20: DCDBD
Aufgaben 21–25: ABCEB
```

Diese Funde sind Wiederveröffentlichungen, kein direkt vom Veranstalter
abgerufener Lösungsschlüssel. Alle 25 Lösungen wurden zusätzlich inhaltlich
nachgerechnet bzw. logisch überprüft. Die deutschen Lösungswege wurden für
dieses Heft neu formuliert.

## Leerer und ausgefüllter Kódlap

Vorlage: [offizieller Muster-Kódlap der MATEGYE Alapítvány](http://www.mategye.hu/download/zrinyi/minta_kodlap.pdf).
Der Server war beim Abruf über HTTP erreichbar, über HTTPS nicht.

Übernommenes Layout: Aufgaben 1–15 links, 16–25 rechts; Fünferblöcke mit den
Spalten A–E und quadratischen Ankreuzfeldern. Die Vorlage hat auch Aufgaben
26–30; diese entfallen für die hier vorliegenden 25 Aufgaben. Beschriftungen
und Ausfüllhinweise sind deutsch. Der leere Bogen steht auf Seite 7, derselbe
Bogentyp mit den Lösungskreuzen auf der letzten Seite (11). Die Formulare
sind zum Ausdrucken und handschriftlichen Ausfüllen gedacht.

## Lokalisierungen

| Original | Deutsche Bearbeitung | Aufgabe |
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
| Anna | Anna (auch ein geläufiger deutscher Name) | 23 |
| Misi, Flóri | Michael, Florian | 24 |

Der Wettbewerb heißt im Aufgabentext „Mathe-Knobelwettbewerb“. Der echte
ungarische Wettbewerbsname und die echten Namen des Herausgebers bleiben
ausschließlich zur nachvollziehbaren Quellenangabe erhalten.

### Sprachabhängige Aufgaben

- **2:** KECSKEMÉT und KALKAR enthalten jeweils genau zwei K; Antwort **C**.
- **15:** LAP → TAL. Der mittlere Buchstabe bleibt A. Ein zusätzliches A
  nach jedem eingegebenen Buchstaben ergibt **TAAALA**, weiterhin Antwort
  **C**. Alle fünf Antwortmöglichkeiten wurden konsistent mit L → T,
  P → L und unverändertem A umgestellt.
- **24:** Statt MÉZES und MÁLNA werden **BLUME und KREIS** genannt. Die
  Antwortmöglichkeiten sind vollständig durch deutsche Wörter ersetzt.
  Alle verwendeten Wörter haben fünf verschiedene Buchstaben, sodass die
  Zählregel auch ohne Sonderregeln zu Buchstabenwiederholungen eindeutig ist.

| Antwort | Wort | Gemeinsam mit BLUME | Gemeinsam mit KREIS |
|---|---|---:|---:|
| A | LAMPE | 3 | 1 |
| B | TIGER | 1 | 3 |
| C | MULDE | 4 | 1 |
| D | STUHL | 2 | 1 |
| **E** | **WOLKE** | **2 (L, E)** | **2 (K, E)** |

  Damit bleiben die beiden Hinweise „2“, die Art des Rätsels und die
  eindeutige richtige Antwort **E** erhalten. Die falschen Wörter und ihre
  jeweiligen Überlappungszahlen sind neu gewählt.

### Wichtige Bedeutungsdetails

- **21:** Die Regionalrunde findet vor dem Finale statt. „Bisher“ umfasst
  daher nur 24 abgeschlossene Wettbewerbsjahre: **24 − 2 − 2 − 1 = 19**,
  Antwort **A**. Dieser im Original zeitlich vorausgesetzte Umstand wird
  ausdrücklich erklärt, damit die zeitlose Übungsfassung eindeutig bleibt.
- **25:** „Neben jedem Stuhl“ betrifft **auch freie Stühle**. Eine Deutung
  nur für besetzte Stühle würde das Problem verändern. Mit der vollständigen
  Regel sind höchstens **6** Plätze besetzt, Antwort **B**. Alle 2¹⁴ möglichen
  Belegungen werden durch das Prüfskript vollständig geprüft.

Die Bearbeitung ist inoffiziell. Rechte an den Originalaufgaben verbleiben
bei den jeweiligen Rechteinhabern; diese Sammlung behauptet keine freie
Lizenz für fremdes Ausgangsmaterial.
