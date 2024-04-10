##Question ID: 658

from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    left = 0
    right = len(arr) - k

    while left < right:
        mid = left + (right - left) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]

## Structure
from typing import List
    # Your code here

    pass