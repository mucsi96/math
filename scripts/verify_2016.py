"""Independent solutions and exhaustive checks for the 2016 booklet."""

from itertools import combinations, permutations, product
from diagrams_2016 import BASKETS, DOMINOES, GRAPHS


def verify_math(data):
    exercises = data["exercises"]
    assert [e["number"] for e in exercises] == list(range(1,26))
    assert all(len(e["options"]) == 5 for e in exercises)
    key = "DBECCEEDEBEDEBADDCBEDDADE"
    assert data["published_answer_key"].replace(" ", "") == key
    assert "".join(e["answer"] for e in exercises) == key
    results = {3:sum(map(int,"1052")), 4:4+2, 5:50-13, 6:7*2,
               7:2*10+5, 8:3*15, 13:10+8+1, 17:15+16//2,
               20:sum(str(n).count("1") for n in range(100)),
               23:len(list(combinations(range(4),2)))}
    # Only two blunt pencils can satisfy both conditions.
    blunt = [n for n in range(6) if 5-n > n and n-1 > 0]
    assert blunt == [2]
    results[10] = blunt[0]-1
    pairs = [(a,b) for a in range(30) for b in range(a,30) if a+b==29 and b-a==5]
    assert pairs == [(12,17)]
    results[15] = sum(map(int,str(pairs[0][0])))
    results[18] = sum(mid < bottom < left and bottom < right
                      for left,mid,right,bottom in permutations([2,0,1,6]))
    results[21] = sum(path.count("R")==2 for path in product("RU",repeat=5))
    assignments = []
    for club,heart,face,diamond,square in permutations(range(10),5):
        if min(club,face,diamond) == 0:
            continue
        a,b,c = 10*club+heart,10*face+club,10*diamond+square
        if b-a == 11 and c-b == 3:
            assignments.append((a,b,c,face))
    assert assignments == [(76,87,90,8)], assignments
    results[22] = assignments[0][3]
    hats = [row for row in product((False,True),repeat=5)
            if sum(row)==2 and row[2]+row[4]==1 and row[3]+row[1]==1]
    statements = [(r,r and b,not r,b and w) for r,w,g,b,y in hats]
    results[25] = sum(len({row[i] for row in statements})==1 for i in range(4))
    for n,value in results.items():
        ex = exercises[n-1]
        assert ex["options"].count(str(value)) == 1, (n,value)
        assert "ABCDE"[ex["options"].index(str(value))] == ex["answer"], n
    assert exercises[0]["options"][3] == "Dreieck"
    # Picture 2: the long hair in B is absent from the target; all other
    # feature sets are subsets of the target. Geometry is visually reviewed.
    target = {"outline","eyes","nose","smile","ears","short hair"}
    partials = [{"outline","eyes","nose","smile","ears"},
                {"outline","eyes","nose","smile","long hair"}, {"outline"},
                {"outline","eyes","nose","smile"}, {"outline","eyes","nose"}]
    assert [i for i,f in enumerate(partials) if not f <= target] == [1]
    assert [i for i,(b,l,a) in enumerate(BASKETS) if a==l+1 and b==a+1] == [4]
    name = "VIOLA"
    swaps = {name[:i]+name[i+1]+name[i]+name[i+2:] for i in range(4)}
    assert len(set(name)) == len(name) == 5
    assert [i for i,w in enumerate(exercises[10]["options"]) if w in swaps] == [4]
    assert all(sorted(w)==sorted(name) for w in exercises[10]["options"])
    # Reflect the cut triangle across both folds: its boundary is a diamond.
    vertices = {(sx*x,sy*y) for sx,sy in product((-1,1),repeat=2)
                for x,y in [(0,1),(1,0)]}
    assert vertices == {(0,1),(1,0),(0,-1),(-1,0)}
    assert exercises[11]["answer"] == "D"
    valid = []
    for i,text in enumerate(exercises[13]["options"]):
        a,b = text.split(" und ")
        s = "374261".translate(str.maketrans({a:b,b:a}))
        if int(s[:2])+int(s[2:4])==int(s[4:]):
            valid.append(i)
    assert valid == [1]
    difference = sum(a-b for a,b in DOMINOES)
    assert [i for i,(a,b) in enumerate(DOMINOES) if difference-2*(a-b)==0] == [3]
    weekdays = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
    assert exercises[18]["options"][1] == weekdays[(4-(19-2))%7]
    # Each word has at most two distinct letters. Eight letters suffice for
    # any four two-letter words, even if repeated letters are allowed.
    # Exhaust the three mutually disjoint leaves of the impossible star.
    words = [frozenset(w) for w in combinations(range(8),2)] + [frozenset([i]) for i in range(8)]
    for center in words:
        leaves = [w for w in words if w & center]
        assert not any(not(a&b or a&c or b&c) for a,b,c in combinations(leaves,3))
    witnesses = [("AB","AC","BD","EF"),("AB","AC","BD","CD"),
                 ("DE","AB","AC","BC"),None,("AB","AC","DE","BD")]
    for edges,example in zip(GRAPHS,witnesses):
        if example:
            actual = {(a,b) for a,b in combinations(range(4),2) if set(example[a]) & set(example[b])}
            assert actual == edges
    assert exercises[23]["answer"] == "D"
    print("PASS: all 25 answers; adjacent-letter swaps; exhaustive arrows, number line, word graphs and hats")
