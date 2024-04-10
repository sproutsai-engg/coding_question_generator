##Question ID: 1779

def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    min_distance = float("inf")
    index = -1
    for i, point in enumerate(points):
        if x == point[0] or y == point[1]:
            distance = abs(x - point[0]) + abs(y - point[1])
            if distance < min_distance:
                min_distance = distance
                index = i
    return index

## Structure
def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    # Your code here

    pass