##Question ID: 987

from collections import deque

def deckRevealedIncreasing(deck):
    n = len(deck)
    index = deque(range(n))
    ans = [0] * n

    deck.sort()
    for card in deck:
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())

    return ans

## Structure
from collections import deque
    # Your code here

    pass