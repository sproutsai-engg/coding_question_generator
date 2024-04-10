##Question ID: 90

from itertools import combinations

def subsetsWithDup(nums):
    result = set()
    nums.sort()
    for i in range(len(nums) + 1):
        for combo in combinations(nums, i):
            result.add(combo)
    return list(result)

## Structure
from itertools import combinations
    # Your code here

    pass