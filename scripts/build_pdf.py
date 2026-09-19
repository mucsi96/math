"""Build the German contest booklet, including blank and completed code sheets."""

import argparse
import json
import math
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "competitions/zrinyi/2014/grade-02/regional"
OUTPUT = BATCH / "mathe-knobelei-2014-klasse-2-regionalrunde.de.pdf"
INK = colors.HexColor("#173c46")
PALE = colors.HexColor("#edf3f4")
WIDTH = A4[0] - 88


def register_fonts(directory):
    for name, filename in (("DejaVu", "DejaVuSans.ttf"), ("DejaVu-Bold", "DejaVuSans-Bold.ttf")):
        path = directory / filename
        if not path.exists():
            raise SystemExit(f"Missing {path}. Install fonts-dejavu-core or use --font-dir.")
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold")


def polygon(c, points, fill=0):
    p = c.beginPath()
    p.moveTo(*points[0])
    for point in points[1:]:
        p.lineTo(*point)
    p.close()
    c.drawPath(p, stroke=1, fill=fill)


def hippo(c):
    c.setFillColor(colors.white)
    for x in (-14, 14):
        c.circle(x, 17, 6, fill=1)
    c.ellipse(-23, -20, 23, 20, fill=1)
    c.ellipse(-25, -20, 25, 5, fill=1)
    c.setFillColor(colors.black)
    for x in (-9, 9):
        c.circle(x, 10, 1.8, stroke=0, fill=1)
    for x in (-13, 13):
        c.circle(x, -5, 1.4, stroke=0, fill=1)
    c.arc(-13, -14, 13, -2, 200, 140)


def lion(c):
    c.setFillColor(colors.white)
    points = []
    for i in range(40):
        r = 28 if i % 2 == 0 else 22
        angle = i * math.pi / 20
        points.append((r * math.cos(angle), r * math.sin(angle)))
    polygon(c, points, fill=1)
    for x in (-13, 13):
        c.circle(x, 13, 5, fill=1)
    c.ellipse(-18, -20, 18, 18, fill=1)
    c.setFillColor(colors.black)
    for x in (-7, 7):
        c.circle(x, 4, 1.6, stroke=0, fill=1)
    polygon(c, [(-4, -2), (4, -2), (0, -7)], fill=1)
    c.line(0, -7, 0, -12)
    c.arc(-9, -14, 0, -7, 190, 150)
    c.arc(0, -14, 9, -7, 200, 150)


def smile(c, x, y):
    c.circle(x, y, 15)
    for dx in (-5, 5):
        c.circle(x + dx, y + 4, 1.2, fill=1)
    c.arc(x - 8, y - 8, x + 8, y + 5, 200, 140)


class Diagram(Flowable):
    HEIGHTS = {"animals": 93, "smile_sum": 54, "triangles_circles": 113,
               "floor_grid": 103, "number_shapes": 68}

    def __init__(self, kind):
        super().__init__()
        self.kind = kind
        self.width = WIDTH
        self.height = self.HEIGHTS[kind]

    def draw(self):
        c = self.canv
        c.setStrokeColor(colors.black)
        c.setFillColor(colors.black)
        c.setLineWidth(1.15)
        if self.kind == "animals":
            for i, rotation in enumerate((0, 90, 180, 0, -90)):
                x = 53 + i * 99
                c.saveState()
                c.translate(x, 52)
                c.rotate(rotation)
                (lion if i == 3 else hippo)(c)
                c.restoreState()
                c.setFont("DejaVu-Bold", 11)
                c.drawCentredString(x, 7, "ABCDE"[i])
        elif self.kind == "smile_sum":
            smile(c, 170, 27)
            smile(c, 250, 27)
            c.setFont("DejaVu", 22)
            c.drawCentredString(210, 19, "+")
            c.drawString(280, 19, "= 6")
        elif self.kind == "triangles_circles":
            x0 = WIDTH / 2 - 42
            for i in range(3):
                x = x0 + 30 * i
                polygon(c, [(x, 85), (x+27, 85), (x+13.5, 108)])
                polygon(c, [(x, 28), (x+27, 28), (x+13.5, 5)])
            for dx, y in ((13.5, 72), (73.5, 72), (43.5, 56), (13.5, 40), (73.5, 40)):
                c.circle(x0+dx, y, 10)
        elif self.kind == "floor_grid":
            x0 = WIDTH / 2 - 44
            for i in range(5):
                c.line(x0+22*i, 6, x0+22*i, 94)
                c.line(x0, 6+22*i, x0+88, 6+22*i)
        elif self.kind == "number_shapes":
            for i, number in enumerate((2, 0, 1, 4)):
                x = 110 + i * 95
                if i == 0:
                    polygon(c, [(x-23, 55), (x+23, 55), (x, 10)])
                    baseline = 34
                elif i == 2:
                    polygon(c, [(x-23, 10), (x+23, 10), (x, 55)])
                    baseline = 21
                else:
                    width = 48 if i == 1 else 45
                    c.rect(x-width/2, 10, width, 45)
                    baseline = 25
                c.setFont("DejaVu", 17)
                c.drawCentredString(x, baseline, str(number))


class CodeSheet(Flowable):
    """Same 1–15 / 16–25 five-row block arrangement as the published Kódlap."""

    def __init__(self, answers=None):
        super().__init__()
        self.answers = answers
        self.width = WIDTH
        self.height = 470

    def draw(self):
        c = self.canv
        c.setStrokeColor(colors.black)
        c.setFillColor(colors.black)
        for start, column, block in ((1, 0, 0), (6, 0, 1), (11, 0, 2), (16, 1, 0), (21, 1, 1)):
            left = column * 267
            top = 441 - block * 151
            c.setFont("DejaVu-Bold", 11)
            for i, letter in enumerate("ABCDE"):
                c.drawCentredString(left + 91 + i*29, top + 15, letter)
            c.setLineWidth(0.65)
            c.rect(left + 76, top - 126, 147, 135)
            for row in range(5):
                number = start + row
                y = top - row * 25 - 10
                c.setFont("DejaVu", 10)
                c.drawRightString(left + 67, y-3, f"{number}.")
                for i, letter in enumerate("ABCDE"):
                    x = left + 83 + i*29
                    c.rect(x, y-8, 16, 16)
                    if self.answers and self.answers[number-1] == letter:
                        c.setLineWidth(1.8)
                        c.line(x+2, y-6, x+14, y+6)
                        c.line(x+2, y+6, x+14, y-6)
                        c.setLineWidth(0.65)
        c.setFont("DejaVu", 9)
        c.drawString(279, 116, "25 Aufgaben · jeweils eine Antwort")
        if not self.answers:
            c.drawString(279, 97, "Viel Freude beim Knobeln!")


def styles():
    return {
        "title": ParagraphStyle("title", fontName="DejaVu-Bold", fontSize=24, leading=30, textColor=INK, spaceAfter=8),
        "subtitle": ParagraphStyle("subtitle", fontName="DejaVu", fontSize=12, leading=17, spaceAfter=14),
        "body": ParagraphStyle("body", fontName="DejaVu", fontSize=12, leading=17, spaceAfter=7),
        "small": ParagraphStyle("small", fontName="DejaVu", fontSize=9, leading=13, spaceAfter=6),
        "solution": ParagraphStyle("solution", fontName="DejaVu", fontSize=10.2, leading=14.5, spaceAfter=10),
        "option": ParagraphStyle("option", fontName="DejaVu", fontSize=10.7, leading=15),
        "table": ParagraphStyle("table", fontName="DejaVu", fontSize=10, leading=13, alignment=TA_CENTER),
    }


def timetable(st):
    rows = [["Stunde", "Montag", "Mittwoch", "Freitag"],
            ["1", "Besenflug", "Zaubersprüche", "Geheimschrift"],
            ["2", "Hellsehen", "Geheimschrift", "Hellsehen"],
            ["3", "Geheimschrift", "Besenflug", "Zaubersprüche"]]
    table = Table([[Paragraph(escape(t), st["table"]) for t in row] for row in rows],
                  colWidths=[55, 140, 140, 140], rowHeights=26)
    table.setStyle(TableStyle([("GRID", (0,0), (-1,-1), .65, colors.black),
                               ("BACKGROUND", (0,0), (-1,0), PALE),
                               ("VALIGN", (0,0), (-1,-1), "MIDDLE")]))
    return table


def options(ex, st):
    cells = [Paragraph(f"<b>({letter})</b> {escape(text)}", st["option"])
             for letter, text in zip("ABCDE", ex["options"])]
    # Longer alternatives get their own lines instead of squeezing the type.
    if max(map(len, ex["options"])) > 13:
        rows, widths = [[cell] for cell in cells], [WIDTH]
    else:
        rows, widths = [cells], [WIDTH / 5] * 5
    t = Table(rows, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0),
                           ("RIGHTPADDING", (0,0), (-1,-1), 7),
                           ("TOPPADDING", (0,0), (-1,-1), 3),
                           ("BOTTOMPADDING", (0,0), (-1,-1), 3),
                           ("VALIGN", (0,0), (-1,-1), "TOP")]))
    return t


def footer(c, doc):
    c.saveState()
    c.setStrokeColor(colors.HexColor("#b8c8cc"))
    c.line(44, 40, A4[0]-44, 40)
    c.setFillColor(INK)
    c.setFont("DejaVu", 8)
    c.drawString(44, 26, "Mathe-Knobelei · Klasse 2 · Regionalrunde 2014")
    c.drawRightString(A4[0]-44, 26, f"Seite {doc.page}")
    c.restoreState()


def build(font_dir):
    register_fonts(font_dir)
    data = json.loads((BATCH / "exercises.de.json").read_text(encoding="utf-8"))
    st = styles()
    story = []
    groups = [(1,5), (6,10), (11,13), (14,17), (18,21), (22,25)]
    for start, end in groups:
        if story:
            story.append(PageBreak())
        story.append(Paragraph(data["title"] if start == 1 else f"Aufgaben {start}–{end}", st["title"]))
        if start == 1:
            story.append(Paragraph(data["subtitle"], st["subtitle"]))
            story.append(Paragraph("Lies genau und kreuze für jede Aufgabe eine Antwort von A bis E an. "
                                   "Deinen Antwortbogen findest du nach den Aufgaben. Du darfst hier rechnen und zeichnen.", st["body"]))
            story.append(Paragraph("Name: ____________________________________    Datum: ______________", st["small"]))
            story.append(Spacer(1, 9))
        else:
            story.append(Spacer(1, 8))
        for ex in data["exercises"][start-1:end]:
            block = [Paragraph(f'<b>{ex["number"]}.</b> {escape(ex["text"])}', st["body"])]
            if diagram := ex.get("diagram"):
                block.append(timetable(st) if diagram == "timetable" else Diagram(diagram))
                block.append(Spacer(1, 6))
            # Animal choices are already labelled directly beneath the pictures.
            if ex.get("diagram") != "animals":
                block.append(options(ex, st))
            block.append(Spacer(1, 22 if start != 1 else 15))
            story.append(KeepTogether(block))

    story.extend([PageBreak(), Paragraph("Mein Antwortbogen", st["title"]),
                  Paragraph("Klasse 2 · 25 Aufgaben · Regionalrunde 2014", st["subtitle"]),
                  Paragraph("Name: __________________________________________________", st["body"]),
                  Paragraph("Schule: ___________________________  Klasse: ______________", st["body"]),
                  Paragraph("Datum: ___________________________  Raum / Platz: __________", st["body"]),
                  Spacer(1, 6),
                  Paragraph("Kreuze pro Aufgabe genau ein Kästchen deutlich an. Verwende einen blauen oder schwarzen Stift. "
                            "Ein großes Kreuz soll das ganze Kästchen ausfüllen.", st["body"]),
                  Spacer(1, 8), CodeSheet(),
                  Paragraph("Deutschsprachiger Übungsbogen nach dem Zrínyi-Kódlap-Muster; "
                            "für diese Klassenstufe auf 25 Aufgaben angepasst.", st["small"])])

    story.extend([PageBreak(), Paragraph("Quellen & Hinweise", st["title"]),
                  Paragraph("Für Eltern und Lehrkräfte", st["subtitle"]),
                  Paragraph("Dieses Heft ist eine eigenständige deutsche Bearbeitung der 25 Aufgaben des "
                            "Zrínyi Ilona Matematikaverseny 2014, 2. Klasse, Megyei forduló (Regionalrunde). "
                            "Die Originalaufgaben stammen von der MATEGYE Alapítvány. Es handelt sich um eine "
                            "inoffizielle Übungsfassung.", st["body"]),
                  Paragraph("Die Originalabbildungen wurden anhand des online verfügbaren Scans neu gezeichnet. "
                            "Der leere und der ausgefüllte Antwortbogen folgen dem offiziellen Kódlap-Muster: "
                            "Aufgaben 1–15 links, 16–25 rechts, Kästchen A–E in Fünferblöcken.", st["body"]),
                  Paragraph("Namen und Orte wurden deutsch lokalisiert. Die Buchstabenaufgaben 2, 15 und 24 "
                            "verwenden passende deutsche Wörter. Bei Aufgabe 21 ist ausdrücklich gesagt, dass das "
                            "diesjährige Finale noch bevorsteht. Bei Aufgabe 25 gilt die Nachbarregel ausdrücklich "
                            "auch für freie Stühle. Alle richtigen Antwortbuchstaben entsprechen dem veröffentlichten Schlüssel.", st["body"]),
                  Spacer(1, 12)])
    for label, url in [
        ("Originalscan und Antwortschlüssel", "https://matekkicsiknek.webnode.hu/zrinyi/"),
        ("Zweiter Fund des Antwortschlüssels", "https://pdfcoffee.com/zrinyi-megoldokulcs-2014-pdf-free.html"),
        ("Offizielles Kódlap-Muster", "http://www.mategye.hu/download/zrinyi/minta_kodlap.pdf"),
        ("Projekt, bearbeitbare Aufgaben und genaue Quellen", "https://github.com/mucsi96/math"),
    ]:
        story.append(Paragraph(f'<b>{label}</b><br/><link href="{url}" color="#173c46">{url}</link>', st["small"]))
    story.extend([Spacer(1, 24), Paragraph("Ab der nächsten Seite: Lösungen", st["title"]),
                  Paragraph("Zum Üben die folgenden Seiten abtrennen oder erst nach dem Bearbeiten ansehen.", st["body"])])

    for start, end in [(1,13), (14,25)]:
        story.extend([PageBreak(), Paragraph(f"Lösungswege {start}–{end}", st["title"]), Spacer(1, 10)])
        for ex in data["exercises"][start-1:end]:
            story.append(Paragraph(f'<b>{ex["number"]}. ({ex["answer"]})</b> {escape(ex["solution"])}', st["solution"]))

    story.extend([PageBreak(), Paragraph("Lösungsbogen", st["title"]),
                  Paragraph("Ausgefüllter Antwortbogen · Klasse 2 · Regionalrunde 2014", st["subtitle"]),
                  Paragraph("Vergleiche die Kreuze mit deinem Antwortbogen. Jede Aufgabe hat genau eine richtige Antwort.", st["body"]),
                  Spacer(1, 22), CodeSheet([ex["answer"] for ex in data["exercises"]]),
                  Spacer(1, 12), Paragraph("Antwortschlüssel zur Kontrolle", st["body"]),
                  Paragraph(data["published_answer_key"], st["body"])])

    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=44, rightMargin=44,
                            topMargin=42, bottomMargin=55, title="Mathe-Knobelei – Klasse 2 – Regionalrunde 2014",
                            author="math · Deutsche Bearbeitung nach MATEGYE", pageCompression=1,
                            invariant=1)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font-dir", type=Path, default=Path("/usr/share/fonts/truetype/dejavu"))
    build(parser.parse_args().font_dir)
