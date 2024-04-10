##Question ID: 1354

from sortedcontainers import SortedSet

def winners_and_losers(matches):
    winners, losers = SortedSet(), SortedSet()

    for winner, loser in matches:
        winners.add(winner)
        losers.add(loser)

    return [list(winners), list(losers)]

## Structure
from sortedcontainers import SortedSet
    # Your code here

    pass