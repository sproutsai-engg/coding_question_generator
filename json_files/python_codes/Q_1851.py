##Question ID: 1851

from bisect import bisect_left

def maxValue(events, k):
    events.sort(key=lambda x: x[1])
    n = len(events)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        start = -1
        for j in range(i - 1, 0, -1):
            if events[j - 1][1] < events[i - 1][0]:
                start = j
                break

        for j in range(1, k + 1):
            if start == -1:
                dp[i][j] = max(dp[i - 1][j], events[i - 1][2])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[start][j - 1] + events[i - 1][2])

    return dp[n][k]


## Structure
from bisect import bisect_left
    # Your code here

    pass