##Question ID: 1906

from functools import lru_cache
from math import gcd

def maxScore(nums):
    n = len(nums)

    @lru_cache(None)
    def dfs(i, j):
        if i > n:
            return 0
        ans = 0
        for k in range(j + 1, n * 2):
            ans = max(ans, dfs(i + 1, k) + i * gcd(nums[j], nums[k]))
        return ans

    return dfs(1, 0)

## Structure
from functools import lru_cache
    # Your code here

    pass