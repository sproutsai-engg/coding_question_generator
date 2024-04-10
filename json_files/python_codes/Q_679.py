##Question ID: 679

from itertools import permutations

def helper(cards, target=24):
    if len(cards) == 1:
        return abs(cards[0] - target) < 1e-6

    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            a, b = cards[i], cards[j]
            rest = [cards[k] for k in range(len(cards)) if k != i and k != j]
            for e in a + b, a - b, a * b, a / b:
                if helper(rest + [e]):
                    return True
    return False

def canGet24(cards):
    return helper(cards)


## Structure
from itertools import permutations
    # Your code here

    pass