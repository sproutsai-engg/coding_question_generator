##Question ID: 1758

from typing import List

def canDistribute(nums: List[int], quantity: List[int]) -> bool:
    counts = [0] * 51
    for num in nums:
        counts[num] += 1

    quantity.sort(reverse=True)

    def dfs(idx: int) -> bool:
        if idx == len(quantity):
            return True
        for i in range(1, 51):
            if counts[i] >= quantity[idx]:
                counts[i] -= quantity[idx]
                if dfs(idx + 1):
                    return True
                counts[i] += quantity[idx]
        return False

    return dfs(0)


## Structure
from typing import List
    # Your code here

    pass