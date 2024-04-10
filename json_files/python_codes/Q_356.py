##Question ID: 356

def isReflected(points):
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    point_set = {(point[0], point[1]) for point in points}
    
    sum_x = min_x + max_x
    for point in points:
        if (sum_x - point[0], point[1]) not in point_set:
            return False

    return True

## Structure
def isReflected(points):
    # Your code here

    pass