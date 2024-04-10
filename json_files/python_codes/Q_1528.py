##Question ID: 1528

from typing import List

def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    max_candies = max(candies)
    result = [candy + extra_candies >= max_candies for candy in candies]
    return result

## Structure
from typing import List
    # Your code here

    pass