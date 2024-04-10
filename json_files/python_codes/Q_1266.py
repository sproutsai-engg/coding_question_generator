##Question ID: 1266

def minTimeToVisitAllPoints(points):
    time = 0
    for i in range(1, len(points)):
        dx = abs(points[i][0] - points[i - 1][0])
        dy = abs(points[i][1] - points[i - 1][1])
        time += max(dx, dy)
    return time

## Structure
def minTimeToVisitAllPoints(points):
    # Your code here

    pass