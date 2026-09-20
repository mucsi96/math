"""Black-and-white vector redraws of the 2015 grade-2 regional paper."""

import math

HEIGHTS = {"pencils": 65, "snowmen": 85, "square_pairs": 122,
           "flowers": 110, "purses": 180, "animal_order": 145}


def polygon(c, points):
    p = c.beginPath()
    p.moveTo(*points[0])
    for point in points[1:]:
        p.lineTo(*point)
    p.close()
    c.drawPath(p)


def animal(c, kind, x, y, scale=1):
    c.saveState()
    c.translate(x, y)
    c.scale(scale, scale)
    if kind == "Maus":
        c.ellipse(-7, 0, 7, 15)
        c.circle(0, 20, 7)
        c.circle(-6, 26, 4)
        c.circle(6, 26, 4)
        c.bezier(6, 3, 18, 1, 15, -4, 9, -3)
        eye_y = 21
    elif kind == "Katze":
        c.ellipse(-10, 0, 10, 23)
        c.circle(0, 29, 11)
        polygon(c, [(-10, 34), (-10, 45), (-2, 40)])
        polygon(c, [(2, 40), (10, 45), (10, 34)])
        c.bezier(9, 4, 25, 10, 8, 24, 20, 28)
        for yy in (26, 30):
            c.line(-5, yy, -16, yy-2)
            c.line(5, yy, 16, yy-2)
        eye_y = 32
    else:
        c.ellipse(-10, 0, 10, 32)
        c.ellipse(-11, 29, 11, 51)
        c.ellipse(-16, 31, -9, 47)
        c.ellipse(9, 31, 16, 47)
        c.ellipse(-6, 31, 6, 38)
        c.line(-6, 3, -6, 15)
        c.line(6, 3, 6, 15)
        c.bezier(9, 5, 27, 15, 14, 22, 19, 16)
        eye_y = 43
    for dx in (-3, 3):
        c.circle(dx, eye_y, .8, fill=1)
    c.restoreState()


def draw(c, kind, width):
    centers = [width*(i+.5)/5 for i in range(5)]
    if kind in ("pencils", "snowmen", "square_pairs"):
        for i, x in enumerate(centers):
            c.setFont("DejaVu-Bold", 11)
            c.drawCentredString(x, 2, "ABCDE"[i])
            if kind == "pencils":
                height = [32, 26, 40, 48, 19][i]
                c.rect(x-4, 16, 8, height-8)
                polygon(c, [(x-4, 8+height), (x+4, 8+height), (x, 16+height)])
                c.line(x-1, 16, x-1, 8+height)
                c.line(x+2, 16, x+2, 8+height)
            elif kind == "snowmen":
                c.circle(x, 43, 22)
                c.rect(x-10, 65, 20, 10)
                c.line(x-27, 65, x+27, 65)
                for dx in (-8, 8):
                    xx, yy = x+dx, 49
                    if i == 0:
                        for angle in (0, 45, 90, 135):
                            a = math.radians(angle)
                            c.line(xx-5*math.cos(a), yy-5*math.sin(a),
                                   xx+5*math.cos(a), yy+5*math.sin(a))
                    elif i in (1, 2):
                        c.rect(xx-4, yy-4, 8, 11 if i == 1 else 8)
                    elif i == 3:
                        c.circle(xx, yy, 5)
                    else:
                        polygon(c, [(xx-5, yy-4), (xx+5, yy-4), (xx, yy+5)])
                direction = 1 if i in (0, 3) else -1
                polygon(c, [(x, 37), (x+36*direction, 29), (x, 31)])
            else:
                s = 19
                if i == 0:
                    c.rect(x-s/2, 20, s, s)
                    c.rect(x-s/2, 39, s, s)
                elif i == 1:
                    r = s/math.sqrt(2)
                    for xx in (x-r, x+r):
                        polygon(c, [(xx-r, 39), (xx, 39+r), (xx+r, 39), (xx, 39-r)])
                elif i == 2:
                    c.rect(x-s, 20, s, s)
                    c.rect(x, 39, s, s)
                elif i == 3:
                    polygon(c, [(x-11, 20), (x+11, 20), (x, 39)])
                    polygon(c, [(x-11, 58), (x+11, 58), (x, 39)])
                else:
                    c.rect(x-s/2, 20, s, s)
                    r = s/math.sqrt(2)
                    polygon(c, [(x, 39), (x-r, 39+r), (x, 39+2*r), (x+r, 39+r)])
        if kind == "square_pairs":
            c.setFont("DejaVu", 10)
            c.drawString(width/2-92, 96, "Deine Quadrate:")
            c.rect(width/2+10, 90, 19, 19)
            c.rect(width/2+37, 90, 19, 19)
    elif kind == "flowers":
        x0 = width/2-78
        c.rect(x0-14, 3, 177, 104)
        for row, bloom in enumerate(((True, False, True, False, True, False),
                                     (True, False, False, True, True, True))):
            y = 62 if row == 0 else 12
            for col, flowering in enumerate(bloom):
                x = x0+col*28
                c.ellipse(x-7, y, x, y+13)
                c.ellipse(x, y, x+7, y+13)
                if flowering:
                    c.line(x, y, x, y+29)
                    for dx, dy in ((-4, 0), (4, 0), (0, 4), (0, -4)):
                        c.circle(x+dx, y+31+dy, 3)
                    c.circle(x, y+31, 2, fill=1)
    elif kind == "purses":
        values = [[50,20,20,10,20], [20]*5, [50,20,10,10],
                  [20,20,10,20,10], [20,10,20,20,20,10]]
        for i, coins in enumerate(values):
            x = [70, 250, 430, 160, 340][i]
            y = 104 if i < 3 else 16
            c.roundRect(x-43, y, 86, 62, 12)
            c.line(x-34, y+62, x+34, y+62)
            c.circle(x-4, y+68, 3)
            c.circle(x+4, y+68, 3)
            c.setFont("DejaVu-Bold", 11)
            c.drawCentredString(x-56, y+27, "ABCDE"[i])
            for j, value in enumerate(coins):
                count_top = 2 if i in (1, 2, 3) else 3
                row = 0 if j < count_top else 1
                col = j if row == 0 else j-count_top
                count = count_top if row == 0 else len(coins)-count_top
                xx = x+(col-(count-1)/2)*26
                yy = y+44-row*27
                c.circle(xx, yy, 11)
                c.setFont("DejaVu", 10)
                c.drawCentredString(xx, yy-3.5, str(value))
    elif kind == "animal_order":
        c.setFont("DejaVu", 10)
        c.drawString(80, 108, "Am Anfang:")
        for x, name in zip((235, 290, 345), ("Katze", "Maus", "Hund")):
            animal(c, name, x, 87, .85)
            c.drawCentredString(x, 76, name)
        orders = [("Hund", "Katze", "Maus"), ("Katze", "Hund", "Maus"),
                  ("Hund", "Maus", "Katze"), ("Maus", "Katze", "Hund"),
                  ("Maus", "Hund", "Katze")]
        for i, (x, names) in enumerate(zip(centers, orders)):
            for dx, name in zip((-28, 0, 28), names):
                animal(c, name, x+dx, 19, .67)
            c.setFont("DejaVu-Bold", 11)
            c.drawCentredString(x, 2, "ABCDE"[i])
