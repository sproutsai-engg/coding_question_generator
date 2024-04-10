##Question ID: 46

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    def helper(index):
        if index == len(nums) - 1:
            results.append(nums[:])
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            helper(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    results = []
    helper(0)
    return results

## Structure
from typing import List
    # Your code here

    pass