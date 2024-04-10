##Question ID: 1799

from typing import List

def minimumIncompatibility(nums: List[int], k: int) -> int:
    n = len(nums)
    if n % k != 0:
        return -1
    
    nums.sort()
    diffs = [nums[(i + 1) * (n // k) - 1] - nums[i * (n // k)] for i in range(k)]
    
    return sum(diffs)

## Structure
from typing import List
    # Your code here

    pass