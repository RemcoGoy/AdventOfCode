from collections import Counter, namedtuple
from functools import cmp_to_key, partial

input_file = open("./input.txt", "r")
lines = input_file.read()

hands = [
    namedtuple("hbtup", "hand bid")(ll[0], int(ll[1]))
    for l in lines.splitlines()
    if (ll := l.split())
]


def ranks1(hand):
    mc = Counter(hand).most_common(2)
    if mc[0][1] == 5:
        return 7
    match [mc[0][1], mc[1][1]]:
        case [4, _]:
            return 6
        case [3, 2]:
            return 5
        case [3, _]:
            return 4
        case [2, 2]:
            return 3
        case [2, _]:
            return 2
    return 1


def ranks2(hand):
    return max(ranks1(hand.replace("J", c)) for c in "23456789TQKA")


def compare_hands(ranks, cardstr, t1, t2):
    r1, r2 = ranks(t1.hand), ranks(t2.hand)
    if r1 > r2:
        return 1
    if r1 < r2:
        return -1
    for a, b in zip(t1.hand, t2.hand):
        if cardstr(a) > cardstr(b):
            return 1
        if cardstr(a) < cardstr(b):
            return -1
    return 0


cmp1 = partial(compare_hands, ranks1, lambda c: "23456789TJQKA".index(c))
cmp2 = partial(compare_hands, ranks2, lambda c: "J23456789TQKA".index(c))

for c in [cmp1, cmp2]:
    ranked = sorted(hands, key=cmp_to_key(c))
    print(sum(i * h.bid for i, h in enumerate(ranked, 1)))


input_file.close()
