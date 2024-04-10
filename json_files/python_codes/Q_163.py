##Question ID: 163

from typing import List

def find_missing_ranges(nums: List[int], lower: int, upper: int) -> List[str]:
    result = []
    prev = lower - 1

    for i, num in enumerate(nums + [upper + 1]):
        if num - prev >= 2:
            result.append(f"{prev + 1}" + ("" if num - prev == 2 else "->") + f"{num - 1}")
        prev = num

    return result

## Structure
from typing import List
    # Your code here

    pass