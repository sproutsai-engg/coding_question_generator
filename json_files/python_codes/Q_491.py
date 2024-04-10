##Question ID: 491

from typing import List

def findSubsequences(nums: List[int]) -> List[List[int]]:
    res = set()
    dfs(nums, 0, [], res)
    return list(res)

def dfs(nums, start, path, res):
    if len(path) >= 2:
        res.add(tuple(path))
    for i in range(start, len(nums)):
        if path and path[-1] > nums[i]:
            continue
        dfs(nums, i + 1, path + [nums[i]], res)

## Structure
from typing import List
    # Your code here

    pass