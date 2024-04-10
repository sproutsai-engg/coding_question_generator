##Question ID: 864

def largestOverlap(img1, img2):
    n = len(img1)
    onesImg1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
    onesImg2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]

    overlaps = {}
    for pt1 in onesImg1:
        for pt2 in onesImg2:
            dx, dy = pt2[0] - pt1[0], pt2[1] - pt1[1]
            key = (dx, dy)
            if key not in overlaps:
                overlaps[key] = 0
            overlaps[key] += 1

    return max(overlaps.values() or [0])

## Structure
def largestOverlap(img1, img2):
    # Your code here

    pass