##Question ID: 830

from itertools import combinations

def largestTriangleArea(points):
    return max(0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))

## Structure
from itertools import combinations
    # Your code here

    pass