##Question ID: 469

def isConvex(points):
    n = len(points)
    pre = cur = 0

    for i in range(n):
        x1 = points[(i + 1) % n][0] - points[i][0]
        y1 = points[(i + 1) % n][1] - points[i][1]
        x2 = points[(i + 2) % n][0] - points[(i + 1) % n][0]
        y2 = points[(i + 2) % n][1] - points[(i + 1) % n][1]
        cur = x1 * y2 - x2 * y1

        if cur == 0:
            continue
        if cur * pre < 0:
            return False
        pre = cur

    return True

## Structure
def isConvex(points):
    # Your code here

    pass