##Question ID: 1014

def kClosest(points, k):
    points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
    return points[:k]

## Structure
def kClosest(points, k):
    # Your code here

    pass