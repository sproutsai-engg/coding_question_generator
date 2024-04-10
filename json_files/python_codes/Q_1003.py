##Question ID: 1003

from collections import defaultdict
from math import sqrt, inf

def minAreaFreeRect(points):
    minArea = inf
    xGroups = defaultdict(set)

    for x, y in points:
        xGroups[x].add(y)

    for x1, ys1 in xGroups.items():
        for x2, ys2 in xGroups.items():
            if x1 == x2:
                continue

            for y1 in ys1:
                for y2 in ys2:
                    if y2 in ys1 and y1 in ys2:
                        area = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * sqrt((x1 - x2) ** 2 + (y1 - y1) ** 2)
                        minArea = min(minArea, area)

    return minArea if minArea != inf else 0


## Structure
from collections import defaultdict
    # Your code here

    pass