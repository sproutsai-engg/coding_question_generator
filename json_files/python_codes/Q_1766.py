##Question ID: 1766

from bisect import bisect_left

def minimum_mountain_removals(nums):
    n = len(nums)
    left, right = [0] * n, [0] * n
    for i in range(n):
        left[i] = bisect_left(left[:i], nums[i])
        right[n - 1 - i] = bisect_left(right[n - i:], nums[n - 1 - i])

    return n - max(left[i] + right[i] for i in range(1, n - 1)) - 1

## Structure
from bisect import bisect_left
    # Your code here

    pass