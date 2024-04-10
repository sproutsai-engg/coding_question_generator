##Question ID: 1778

from functools import lru_cache

def getMaxGridHappiness(m, n, introvertsCount, extrovertsCount):
    @lru_cache(None)
    def maxHappy(y, mask):
        if y == n:
            return 0

        ans = 0
        for x in range(m + 1):
            happiness = 0
            if mask >> x & 1:
                happiness -= 30
                if x > 0 and mask & 1:
                    happiness -= 30
                else:
                    happiness += 20
            ans = max(ans, happiness + maxHappy(y + 1, (mask | (1 << x)) >> 1))

        return ans

    return maxHappy(0, 0)


## Structure
from functools import lru_cache
    # Your code here

    pass