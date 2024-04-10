##Question ID: 1395

def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    time = 0
    for i in range(1, len(points)):
        dx = abs(points[i][0] - points[i-1][0])
        dy = abs(points[i][1] - points[i-1][1])
        time += max(dx, dy)
    return time


## Structure
def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    # Your code here

    pass