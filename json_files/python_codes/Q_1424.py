##Question ID: 1424

from collections import deque

def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
    max_candies = 0
    visited = set()
    to_process = deque(initialBoxes)

    while to_process:
        box = to_process.popleft()

        if box in visited:
            continue

        visited.add(box)

        if status[box]:
            max_candies += candies[box]
            for key in keys[box]:
                status[key] = 1
                if key in visited:
                    to_process.append(key)
            for contained in containedBoxes[box]:
                to_process.append(contained)
        else:
            to_process.append(box)

    return max_candies

## Structure
from collections import deque
    # Your code here

    pass