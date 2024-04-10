##Question ID: 1881

from itertools import combinations

def minAbsDifference(nums, goal):
    n = len(nums)
    left = nums[:n//2]
    right = nums[n//2:]

    sums_left = set()

    for i in range(len(left) + 1):
        for comb in combinations(left, i):
            sums_left.add(sum(comb))

    ans = abs(goal)

    for i in range(len(right) + 1):
        for comb in combinations(right, i):
            sum_r = sum(comb)
            sum_goal = goal - sum_r
            sum_l = min(sums_left, key=lambda x: abs(x - sum_goal))

            ans = min(ans, abs(sum_l + sum_r - goal))

    return ans

## Structure
from itertools import combinations
    # Your code here

    pass