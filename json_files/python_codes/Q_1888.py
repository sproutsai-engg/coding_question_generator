##Question ID: 1888

def nearestValidPoint(x, y, points):
    min_distance = float('inf')
    min_index = -1

    for i, point in enumerate(points):
        if x == point[0] or y == point[1]:
            distance = abs(x - point[0]) + abs(y - point[1])
            if distance < min_distance:
                min_distance = distance
                min_index = i

    return min_index

## Structure
def nearestValidPoint(x, y, points):
    # Your code here

    pass