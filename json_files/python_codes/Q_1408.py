##Question ID: 1408

import math

def smallest_divisor(nums, threshold):
    left, right = 1, 10**6
    while left < right:
        mid = (left + right) // 2
        total = sum(math.ceil(n / mid) for n in nums)
        if total > threshold:
            left = mid + 1
        else:
            right = mid
    return left

## Structure
import math
    # Your code here

    pass