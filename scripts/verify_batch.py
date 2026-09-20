"""Check mathematics, localization invariants, PDF layout, and actual answer marks."""

import itertools
import json
import re
import argparse
from pathlib import Path

import pymupdf

from build_pdf import BATCH


def verify_2014_math(data):
    exercises = data["exercises"]
    assert [e["number"] for e in exercises] == list(range(1, 26))
    assert all(len(e["options"]) == 5 for e in exercises)
    key = "DCBCDEBBECBDCBCDCDBDABCEB"
    assert "".join(e["answer"] for e in exercises) == key
    assert data["published_answer_key"].replace(" ", "") == key

    # Independent calculations select an option, rather than trusting the stored key.
    numeric = {
        2: "KALKAR".count("K"), 3: 6//2, 4: 5-2, 7: 6-5, 8: 7+2,
        9: 4*4, 10: 47-9,
        11: sum(sides == number for sides, number in [(3,2), (4,0), (3,1), (4,4)]),
        12: 8//2*3, 13: (30-12)//2, 16: 18//3*2, 17: 6//2*6,
        18: 8*60-(7*60+5+5),
        19: sum(a == b for a, b in itertools.product("469", repeat=2)),
        21: (25-1)-2-2-1,
    }
    timetable = ["Besenflug", "Zaubersprüche", "Geheimschrift", "Hellsehen",
                 "Geheimschrift", "Hellsehen", "Geheimschrift", "Besenflug", "Zaubersprüche"]
    numeric[14] = sum(subject in ("Geheimschrift", "Besenflug") for subject in timetable)
    guests = [n for n in range(40) if (n > 6) + (n > 5) == 1]
    assert guests == [6]
    numeric[23] = guests[0]
    # Exhaust all 16,384 arrangements, including the rule for EMPTY chairs.
    def valid_seating(row):
        return all((i > 0 and row[i-1] == 0) or (i < len(row)-1 and row[i+1] == 0)
                   for i in range(len(row)))
    numeric[25] = max(sum(row) for row in itertools.product((0,1), repeat=14) if valid_seating(row))
    example = tuple(int(s == "B") for s in "B F F B B F F B B F F B F F".split())
    assert valid_seating(example) and sum(example) == numeric[25]
    for number, result in numeric.items():
        ex = exercises[number-1]
        assert ex["options"].count(str(result)) == 1, (number, result)
        assert "ABCDE"[ex["options"].index(str(result))] == ex["answer"], number

    assert exercises[0]["answer"] == "D"  # Source and redrawn animals visually reviewed.
    truths = [9-7 == 4, 8 < 6, 8-8 == 8, 9 > 2, 10 == 6+3]
    assert truths == [letter == exercises[4]["answer"] for letter in "ABCDE"]
    weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    assert exercises[5]["options"]["ABCDE".index(exercises[5]["answer"])] == weekdays[(3+2) % 7]
    typed = "".join(letter + "A" for letter in "TAL")
    assert exercises[14]["options"].index(typed) == 2
    animals = ["Eule", "Fuchs", "Pavian", "Löwe"]
    winners = [animal for animal in animals if not any([animal == "Fuchs", animal == "Fuchs",
                                                       animal == "Eule", animal == "Pavian"])]
    assert winners == ["Löwe"] and exercises[19]["answer"] == "D"
    assert 2/2 == 1 and exercises[21]["options"][1] == "1 Stunde"
    guesses = ["BLUME", "KREIS"]
    counts = [[len(set(word) & set(guess)) for guess in guesses] for word in exercises[23]["options"]]
    assert all(len(set(word)) == 5 for word in guesses + exercises[23]["options"])
    assert [i for i, pair in enumerate(counts) if pair == [2,2]] == [4]
    print("PASS: all 25 answers; German letter/word puzzles; exhaustive seating check")


def main(batch=BATCH, render_dir=None):
    data = json.loads((batch / "exercises.de.json").read_text(encoding="utf-8"))
    year = data["source_year"]
    if year == 2014:
        verify_2014_math(data)
    elif year == 2015:
        from verify_2015 import verify_math
        verify_math(data)
    else:
        raise ValueError(f"No independent mathematics checks for {year}")
    key = data["published_answer_key"].replace(" ", "")
    doc = pymupdf.open(batch / f"mathe-knobelei-{year}-klasse-2-regionalrunde.de.pdf")
    texts = [page.get_text() for page in doc]
    expected_groups = data.get("exercise_pages", [(1,5), (6,10), (11,13), (14,17), (18,21), (22,25)])
    count = len(expected_groups)
    assert len(doc) == count+5, f"Unexpected pagination: {len(doc)} pages"
    for index, (start, end) in enumerate(expected_groups):
        assert [int(n) for n in re.findall(r"^(\d+)\. ", texts[index], re.M)] == list(range(start,end+1))
    assert "Mein Antwortbogen" in texts[count]
    assert "Quellen & Hinweise" in texts[count+1]
    assert "Lösungswege 1–13" in texts[count+2] and "Lösungswege 14–25" in texts[count+3]
    assert "Lösungsbogen" in texts[-1]
    for forbidden in ["Kecskemét", "Veszprém", "Székesfehérvár", "MÉZES", "MÁLNA", "Tudorka", "Misi", "Flóri"]:
        assert forbidden not in "".join(texts[:count+1]), forbidden
    for page in doc:
        assert abs(page.rect.width-595.276) < .01 and abs(page.rect.height-841.89) < .01
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    rect = pymupdf.Rect(span["bbox"])
                    assert page.rect.contains(rect), (page.number+1, span["text"])
                    assert "�" not in span["text"]
        for font in page.get_fonts():
            if "DejaVu" in font[3]:
                assert doc.extract_font(font[0])[3], "Font not embedded"
        if render_dir:
            render_dir.mkdir(parents=True, exist_ok=True)
            page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(render_dir / f"page-{page.number+1:02}.png")

    # Read the drawn boxes and crosses from the PDF itself, not from CodeSheet state.
    for index, filled in [(count, False), (count+4, True)]:
        items = [item for path in doc[index].get_drawings() for item in path["items"]]
        boxes = [item[1] for item in items if item[0] == "re"
                 and abs(item[1].width-16) < .01 and abs(item[1].height-16) < .01]
        diagonals = [item for item in items if item[0] == "l"
                     and abs(abs(item[2].x-item[1].x)-12) < .01
                     and abs(abs(item[2].y-item[1].y)-12) < .01]
        assert len(boxes) == 125
        assert len(diagonals) == (50 if filled else 0)
        # Column-major order gives 1–15, then 16–25.
        boxes.sort(key=lambda r: (r.x0 > 300, round(r.y0, 2), r.x0))
        if filled:
            decoded = ""
            for offset in range(0,125,5):
                marks = []
                for i, box in enumerate(boxes[offset:offset+5]):
                    if sum(box.contains(line[1]) and box.contains(line[2]) for line in diagonals) == 2:
                        marks.append("ABCDE"[i])
                assert len(marks) == 1
                decoded += marks[0]
            assert decoded == key, decoded
    print(f"PASS: {len(doc)} A4 pages; exercise placement; embedded fonts; no clipped text")
    print("PASS: blank Kódlap has 125 unmarked boxes; final Kódlap has the correct 25 crosses")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", type=Path, default=BATCH)
    parser.add_argument("--render-dir", type=Path)
    args = parser.parse_args()
    main(args.batch, args.render_dir)
