##Question ID: 1200

from typing import List

def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    arr.sort()
    min_diff = min(arr[i] - arr[i - 1] for i in range(1, len(arr)))

    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == min_diff:
            result.append([arr[i - 1], arr[i]])

    return result

## Structure
from typing import List
    # Your code here

    pass