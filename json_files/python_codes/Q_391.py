##Question ID: 391

def isRectangleCover(rectangles):
    area = 0
    points = set()
    lx, ly, rx, ry = float('inf'), float('inf'), float('-inf'), float('-inf')

    for rect in rectangles:
        lx, ly = min(lx, rect[0]), min(ly, rect[1])
        rx, ry = max(rx, rect[2]), max(ry, rect[3])

        area += (rect[2] - rect[0]) * (rect[3] - rect[1])

        p1, p2, p3, p4 = (rect[0], rect[1]), (rect[0], rect[3]), (rect[2], rect[1]), (rect[2], rect[3])

        points ^= {p1, p2, p3, p4}

    return len(points) == 4 and area == (rx - lx) * (ry - ly) and (lx, ly) in points and \
           (lx, ry) in points and (rx, ly) in points and (rx, ry) in points

## Structure
def isRectangleCover(rectangles):
    # Your code here

    pass