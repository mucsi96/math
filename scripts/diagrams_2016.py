"""Vector redraws of the 2016 regional paper, grade 2."""

import math
from reportlab.lib import colors

HEIGHTS = {f"2016_{k}": h for k, h in {
    "shapes": 65, "faces": 145, "baskets": 95, "fold": 140,
    "dominoes": 100, "arrows": 105, "grid": 115,
    "numberline": 65, "graphs": 90,
}.items()}
DOMINOES = [(3, 6), (4, 5), (1, 4), (3, 5), (6, 1)]
# Bottles, loaves, apples, in original option order.
BASKETS = [(2, 2, 3), (2, 1, 2), (2, 2, 1), (3, 1, 1), (3, 1, 2)]
GRAPHS = [{(0,1),(0,2)}, {(0,1),(0,2),(1,3),(2,3)},
          {(1,2),(1,3),(2,3)}, {(0,1),(0,2),(0,3)}, {(0,1),(0,3),(2,3)}]


def poly(c, points, fill=0):
    p = c.beginPath()
    p.moveTo(*points[0])
    for point in points[1:]:
        p.lineTo(*point)
    p.close()
    c.drawPath(p, fill=fill, stroke=1)


def label(c, x, text, y=3):
    c.setFillColor(colors.black)
    c.setFont("DejaVu-Bold", 11)
    c.drawCentredString(x, y, text)


def face(c, x, y, features):
    c.circle(x, y, 20)
    if "eyes" in features:
        for dx in (-7, 7):
            c.circle(x+dx, y+4, 1.8, fill=1)
        c.arc(x-3, y-3, x+3, y+3, 0, 180)
    if "smile" in features:
        c.arc(x-12, y-11, x+12, y+9, 205, 130)
    if "ears" in features:
        c.arc(x-26, y-5, x-14, y+7, 90, 180)
        c.arc(x+14, y-5, x+26, y+7, -90, 180)
    if "short" in features:
        for dx in (-12, -6, 0, 6, 12):
            c.bezier(x, y+20, x+dx, y+32, x+dx, y+23, x+dx, y+14)
    if "long" in features:
        for side in (-1, 1):
            for offset in (0, 5, 10):
                c.bezier(x, y+20, x+side*(25+offset), y+30,
                         x+side*20, y-25, x+side*(25+offset), y-25)


def arrow(c, x1, y1, x2, y2):
    c.line(x1, y1, x2, y2)
    a = math.atan2(y2-y1, x2-x1)
    for d in (-.45, .45):
        c.line(x2, y2, x2-7*math.cos(a+d), y2-7*math.sin(a+d))


def draw(c, kind, width):
    xs = [50+i*101 for i in range(5)]
    if kind == "2016_shapes":
        c.rect(xs[0]-24, 22, 48, 29)
        c.circle(xs[1], 38, 19)
        c.wedge(xs[2]-24, 16, xs[2]+24, 64, 0, 180, fill=0)
        poly(c, [(xs[3]-22,22),(xs[3]+22,22),(xs[3],59)])
        x = xs[4]
        poly(c, [(x-7,20),(x+7,20),(x+7,33),(x+20,33),(x+20,47),
                 (x+7,47),(x+7,60),(x-7,60),(x-7,47),(x-20,47),(x-20,33),(x-7,33)])
    elif kind == "2016_faces":
        face(c, width/2, 110, {"eyes","smile","ears","short"})
        label(c, width/2+95, "Leos fertiges Bild", 106)
        for x, features in zip(xs, [{"eyes","smile","ears"}, {"eyes","smile","long"},
                                    set(), {"eyes","smile"}, {"eyes"}]):
            face(c, x, 43, features)
    elif kind == "2016_baskets":
        for x, (bottles, breads, apples) in zip(xs, BASKETS):
            c.arc(x-45, 18, x+45, 72, 180, 180)
            left = x-40
            for i in range(bottles):
                a = left+12*i
                poly(c, [(a,30),(a+9,30),(a+9,57),(a+6,65),(a+6,74),
                         (a+3,74),(a+3,65),(a,57)])
            left += bottles*12
            for i in range(breads):
                a = left+12*i
                c.ellipse(a, 30, a+10, 74)
                for y in (40,49,58,65):
                    c.line(a+2,y,a+8,y+4)
            left += breads*12
            for i in range(apples):
                a, y = left+6+(i//2)*12, 37+(i%2)*19
                c.circle(a, y, 6)
                c.line(a,y+5,a+2,y+10)
    elif kind == "2016_fold":
        x, y = width/2-20, 90
        c.setFillColor(colors.lightgrey)
        c.wedge(x-38,y-38,x+38,y+38,0,90,fill=1)
        c.setDash(3,3)
        c.line(x,y+18,x+18,y)
        c.setDash()
        label(c, x-85, "Schnitt", y+10)
        for i,x in enumerate(xs):
            c.setFillColor(colors.lightgrey)
            c.circle(x,38,25,fill=1)
            c.setFillColor(colors.white)
            if i == 0:
                c.line(x,48,x+12,36)
            elif i == 1:
                c.line(x-12,50,x+12,26)
                c.line(x-12,26,x+12,50)
            elif i == 2:
                poly(c, [(x,38),(x,51),(x+13,38)],1)
            elif i == 3:
                poly(c, [(x,52),(x+14,38),(x,24),(x-14,38)],1)
            else:
                poly(c, [(x,38),(x,51),(x+13,38)],1)
                poly(c, [(x,38),(x,25),(x-13,38)],1)
    elif kind == "2016_dominoes":
        positions = {1:[(0,0)],3:[(-8,-8),(0,0),(8,8)],
                     4:[(-8,-8),(-8,8),(8,-8),(8,8)],
                     5:[(-8,-8),(-8,8),(0,0),(8,-8),(8,8)],
                     6:[(a,b) for a in (-8,8) for b in (-9,0,9)]}
        for x,(top,bottom) in zip(xs,DOMINOES):
            c.rect(x-17,20,34,68)
            c.line(x-17,54,x+17,54)
            for n,y in [(top,71),(bottom,37)]:
                for dx,dy in positions[n]:
                    c.circle(x+dx,y+dy,2.2,fill=1)
    elif kind == "2016_arrows":
        x = width/2
        for a,b in [(x-42,83),(x,83),(x+42,83),(x,18)]:
            c.circle(a,b,15)
        arrow(c,x,67,x,34)
        arrow(c,x-10,32,x-32,69)
        arrow(c,x+10,32,x+32,69)
        return
    elif kind == "2016_grid":
        x,y = width/2-30,18
        for i in range(3):
            c.line(x+30*i,y,x+30*i,y+90)
        for j in range(4):
            c.line(x,y+30*j,x+60,y+30*j)
        label(c,x-83,"Schneckendorf",y-3)
        label(c,x+134,"Schneckenberg",y+86)
        for a,b in [(x,y),(x+60,y+90)]:
            c.circle(a,b,3,fill=1)
        return
    elif kind == "2016_numberline":
        arrow(c,65,43,443,43)
        for i in range(17):
            x = 75+i*22
            c.line(x,39,x,47)
        c.setFont("DejaVu",17)
        for i,text in [(1,"♣♥"),(12,"☺♣"),(15,"♦■")]:
            x = 75+i*22
            c.line(x-4,39,x+4,47)
            c.line(x-4,47,x+4,39)
            c.drawCentredString(x,15,text)
        return
    elif kind == "2016_graphs":
        for x,edges in zip(xs,GRAPHS):
            pts = [(x,77),(x-25,49),(x+25,49),(x,21)]
            for a,b in edges:
                c.line(*pts[a],*pts[b])
            for a,b in pts:
                c.circle(a,b,2.5,fill=1)
    for x,letter in zip(xs,"ABCDE"):
        label(c,x,letter)
