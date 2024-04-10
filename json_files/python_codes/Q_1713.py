##Question ID: 1713

from bisect import bisect_left

def minOperations(target, arr):
    pos = {x: i for i, x in enumerate(target)}

    dp = []
    for a in arr:
        if a in pos:
            idx = bisect_left(dp, pos[a])
            if idx == len(dp):
                dp.append(pos[a])
            else:
                dp[idx] = pos[a]
    return len(target) - len(dp)

## Structure
from bisect import bisect_left
    # Your code here

    pass