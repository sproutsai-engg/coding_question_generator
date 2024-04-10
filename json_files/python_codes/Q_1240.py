##Question ID: 1240

from functools import lru_cache

def stoneGameII(piles):
    n = len(piles)
    for i in range(n - 2, -1, -1):
        piles[i] += piles[i + 1]

    @lru_cache(None)
    def search(idx, M):
        if idx + 2 * M >= n:
            return piles[idx]
        return max(piles[idx] - search(idx + x, max(M, x)) for x in range(1, 2 * M + 1))

    return search(0, 1)

## Structure
from functools import lru_cache
    # Your code here

    pass