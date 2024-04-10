##Question ID: 149

from math import gcd
from collections import defaultdict

def maxPoints(points):
    n = len(points)
    if n <= 2:
        return n

    max_count = 0

    for i in range(n):
        slope_map = defaultdict(int)
        duplicates = 0
        local_max = 0

        for j in range(i+1, n):
            deltaX = points[j][0] - points[i][0]
            deltaY = points[j][1] - points[i][1]

            if deltaX == 0 and deltaY == 0:
                duplicates += 1
                continue

            g = gcd(deltaX, deltaY)
            deltaX = deltaX // g
            deltaY = deltaY // g

            key = f"{deltaX}_{deltaY}"
            slope_map[key] += 1
            local_max = max(local_max, slope_map[key])

        max_count = max(max_count, local_max + duplicates + 1)

    return max_count


## Structure
from math import gcd
    # Your code here

    pass