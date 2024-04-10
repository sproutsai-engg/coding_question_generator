##Question ID: 489

from math import comb

def kthSmallestPath(destination, k):
    row, col = destination
    ans = ""

    for i in range(row + col):
        if row == 0:
            ans += 'H'
            col -= 1
        elif col == 0:
            ans += 'V'
            row -= 1
        elif k <= comb(row + col - 1, row - 1):
            ans += 'H'
            col -= 1
        else:
            ans += 'V'
            k -= comb(row + col - 1, row - 1)
            row -= 1

    return ans


## Structure
from math import comb
    # Your code here

    pass