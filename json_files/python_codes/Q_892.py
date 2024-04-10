##Question ID: 892

from collections import deque

def shortest_subarray(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    res = n + 1
    dq = deque()
    for i in range(n + 1):
        while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
            res = min(res, i - dq.popleft())
        while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
            dq.pop()
        dq.append(i)

    return res if res <= n else -1

## Structure
from collections import deque
    # Your code here

    pass