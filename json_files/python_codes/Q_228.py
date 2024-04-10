##Question ID: 228

from typing import List

def find_ranges(nums: List[int]) -> List[str]:
    result = []
    n = len(nums)
    if n == 0: 
        return result

    start = nums[0]
    for i in range(1, n):
        if nums[i] > nums[i-1] + 1:
            if start == nums[i-1]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(nums[i-1]))
            start = nums[i]

    if start == nums[n-1]:
        result.append(str(start))
    else:
        result.append(str(start) + "->" + str(nums[n-1]))

    return result

## Structure
from typing import List
    # Your code here

    pass