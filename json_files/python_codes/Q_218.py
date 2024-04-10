##Question ID: 218

from sortedcontainers import SortedList

def getSkyline(buildings):
    points = []
    for l, r, h in buildings:
        points.append((l, -h))
        points.append((r, h))
    points.sort()
    heights = SortedList([0])
    prev = 0
    skyline = []
    for x, h in points:
        if h < 0:
            heights.add(-h)
        else:
            heights.remove(h)
        cur = heights[-1]
        if cur != prev:
            skyline.append([x, cur])
            prev = cur
    return skyline

## Structure
from sortedcontainers import SortedList
    # Your code here

    pass