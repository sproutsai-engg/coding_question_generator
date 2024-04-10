##Question ID: 1733

from math import atan2, degrees

def visiblePoints(points, angle, location):
    angles = [degrees(atan2(y - location[1], x - location[0])) for x, y in points if [x, y] != location]
    angles.sort()
    angles += [a + 360 for a in angles]
    n = len(angles)
    max_points, j = 0, 0
    for i in range(2 * n):
        while angles[i] - angles[j] > angle:
            j += 1
        max_points = max(max_points, i - j + 1)
    return max_points + points.count(location)


## Structure
from math import atan2, degrees
    # Your code here

    pass