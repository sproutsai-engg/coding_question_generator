##Question ID: 805

from typing import List

def escape_ghosts(ghosts: List[List[int]], target: List[int]) -> bool:
    max_dist = abs(target[0]) + abs(target[1])
    for ghost in ghosts:
        ghost_dist = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
        if ghost_dist <= max_dist:
            return False
    return True


## Structure
from typing import List
    # Your code here

    pass