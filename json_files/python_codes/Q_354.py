##Question ID: 354

from bisect import bisect_left

def max_envelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    
    for _, h in envelopes:
        idx = bisect_left(dp, h)
        if idx == len(dp):
            dp.append(h)
        else:
            dp[idx] = h

    return len(dp)

## Structure
from bisect import bisect_left
    # Your code here

    pass