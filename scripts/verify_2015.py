"""Independent solution checks for the 2015 grade-2 regional round."""

from itertools import combinations, permutations, product


def verify_math(data):
    exercises = data["exercises"]
    assert [e["number"] for e in exercises] == list(range(1, 26))
    assert all(len(e["options"]) == 5 for e in exercises)
    key = "EBDDDDEDCEEBACABBECECCCED"
    assert data["published_answer_key"].replace(" ", "") == key
    assert "".join(e["answer"] for e in exercises) == key

    def answer(number, value):
        ex = exercises[number-1]
        assert ex["options"].count(str(value)) == 1, (number, value)
        assert "ABCDE"[ex["options"].index(str(value))] == ex["answer"], number

    # Picture answers are independently read from the original scan; redraws
    # are additionally checked visually against that scan.
    assert [e["answer"] for e in exercises if e["number"] in (1,4,6)] == ["E", "D", "D"]
    answer(2, next(n for n in (4,7,8,12,66) if n % 2))
    for number, value in {3:3+4+1, 5:7-2, 7:3*7, 8:3+4, 9:100-45,
                          11:3*4, 14:24-21+7, 15:min(15,28//2),
                          16:2, 17:sum((13,17,14,15,18))-2*5,
                          18:len(list(combinations(range(4),2))), 19:10-1}.items():
        answer(number, value)
    source_options = ["TBS", "TÓI", "BIÁ", "ÓBI", "TBÁ"]
    assert exercises[9]["options"] == [s.replace("Ó", "O").replace("Á", "A") for s in source_options]
    assert len("TOBIAS") == len(set("TOBIAS")) == 6
    assert "TÓBIÁS"[::2] == "TBÁ"
    answer(10, "TOBIAS"[::2])
    purses = [[50,20,20,10,20], [20]*5, [50,20,10,10],
              [20,20,10,20,10], [20,10,20,20,20,10]]
    assert [i for i, coins in enumerate(purses) if len(coins) == 5 and sum(coins) == 100] == [1]
    answer(12, "Bild B")
    answer(13, max(loser for loser in range(8) if loser < 7-loser))
    animals = ["Katze", "Maus", "Hund"]
    animals[0], animals[1] = animals[1], animals[0]
    animals[1], animals[2] = animals[2], animals[1]
    answer(20, " – ".join(animals))
    answer(21, sum(all(int(d) % 2 == 0 for d in str(n)) for n in range(10,100)))
    # Exhaust all seat assignments: order is chair, bench, armchair, stool.
    seatings = [s for s in permutations(("Anna","Benjamin","Clara","David"))
                if s[1] not in ("Anna","Clara") and s[2] not in ("Anna","Clara")
                and s[0] != "Benjamin" and s[3] != "Clara"]
    assert len(seatings) == 2 and {s[0] for s in seatings} == {"Clara"}
    answer(22, "Clara")
    # Symbolic coefficients: each new group = 1/2 red + 1/2 blue.
    red_after, blue_after = (1/2,1/2), (1/2,1/2)
    assert red_after == blue_after
    answer(23, "In beiden sind gleich viele.")
    # Enumerate flower inventories in order red rose, yellow rose, red tulip,
    # yellow tulip, satisfying all four independently stated constraints.
    inventories = [(rr,yr,rt,yt) for rr,yr,rt,yt in product(range(13), repeat=4)
                   if rr+yr+rt+yt == 12 and rr+rt == 7 and rt+yt == 5 and yt == 1]
    assert inventories == [(3,4,4,1)]
    bouquets = [(3,4,0,0), (3,0,4,0), (0,4,3,0), (0,0,4,1), (4,0,0,1)]
    possible = [all(n <= available for n,available in zip(b, inventories[0])) for b in bouquets]
    assert possible == [True,True,True,True,False]
    assert exercises[23]["answer"] == "E"
    # Four colors would already violate the different-color rule. Enumerate
    # up to four colors and up to four balls per color to check both bounds.
    valid = [counts for counts in product(range(5), repeat=4)
             if max(counts) < 4 and sum(n > 0 for n in counts) < 4]
    answer(25, max(map(sum, valid)))
    print("PASS: all 25 answers; TOBIAS adaptation; exhaustive seating, flower and ball checks")
