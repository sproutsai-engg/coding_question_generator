##Question ID: 1726

from math import sqrt

def best_coordinate(towers, radius):
    max_quality = 0
    best_x, best_y = 0, 0

    for x in range(51):
        for y in range(51):
            sum_quality = 0
            for tower in towers:
                dist = sqrt((x - tower[0])**2 + (y - tower[1])**2)
                if dist <= radius:
                    sum_quality += tower[2] // (1 + dist)
            if sum_quality > max_quality:
                max_quality = sum_quality
                best_x, best_y = x, y

    return [best_x, best_y]

## Structure
from math import sqrt
    # Your code here

    pass