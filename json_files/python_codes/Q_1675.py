##Question ID: 1675

from typing import List

def can_place_balls(force: int, position: List[int], m: int) -> bool:
    last_position = position[0]
    placed_balls = 1

    for i in range(1, len(position)):
        if position[i] - last_position >= force:
            placed_balls += 1
            last_position = position[i]

            if placed_balls == m:
                return True

    return False

def max_distance(position: List[int], m: int) -> int:
    position.sort()

    left = 1
    right = position[-1] - position[0]
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_balls(mid, position, m):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

## Structure
from typing import List
    # Your code here

    pass