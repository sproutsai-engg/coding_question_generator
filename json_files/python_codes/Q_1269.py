##Question ID: 1269

from functools import lru_cache

mod = 10**9 + 7

def numOfWays(steps: int, arrLen: int) -> int:
    @lru_cache(None)
    def dp(s, p):
        if p < 0 or p >= arrLen or p > steps - p:
            return 0
        if s == 0:
            return p == 0
        return (dp(s - 1, p - 1) + dp(s - 1, p) + dp(s - 1, p + 1)) % mod

    return dp(steps, 0)


## Structure
from functools import lru_cache
    # Your code here

    pass