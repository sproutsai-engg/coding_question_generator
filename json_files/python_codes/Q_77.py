##Question ID: 77

from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            result.append(current_combination[:])

        for i in range(start, n + 1):
            current_combination.append(i)
            backtrack(i + 1, current_combination)
            current_combination.pop()

    result = []
    backtrack(1, [])
    return result

## Structure
from typing import List
    # Your code here

    pass