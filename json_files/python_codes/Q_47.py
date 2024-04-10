##Question ID: 47

from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[start]:
                continue
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    nums.sort()
    result = []
    backtrack(0)
    return result


## Structure
from typing import List
    # Your code here

    pass