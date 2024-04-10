##Question ID: 1401

def checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2):
    xClosest = max(x1, min(xCenter, x2))
    yClosest = max(y1, min(yCenter, y2))
    return (xCenter - xClosest) ** 2 + (yCenter - yClosest) ** 2 <= radius ** 2

## Structure
def checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2):
    # Your code here

    pass