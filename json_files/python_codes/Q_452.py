##Question ID: 452

def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > end:
            arrows += 1
            end = points[i][1]

    return arrows

## Structure
def findMinArrowShots(points):
    # Your code here

    pass