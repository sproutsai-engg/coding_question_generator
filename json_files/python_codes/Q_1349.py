##Question ID: 1349

from typing import List

def checkStraightLine(coordinates: List[List[int]]) -> bool:
    dx = coordinates[1][0] - coordinates[0][0]
    dy = coordinates[1][1] - coordinates[0][1]

    for x, y in coordinates[2:]:
        if dx * (y - coordinates[0][1]) != dy * (x - coordinates[0][0]):
            return False

    return True

## Structure
from typing import List
    # Your code here

    pass