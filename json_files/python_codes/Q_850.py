##Question ID: 850

def rectangleArea(rectangles):
    mod = 10**9 + 7
    n = len(rectangles)
    X, Y = set(), set()
    for rect in rectangles:
        X.add(rect[0])
        X.add(rect[2])
        Y.add(rect[1])
        Y.add(rect[3])
    sorted_x = sorted(X)
    sorted_y = sorted(Y)
    cnt = [[0 for _ in range(len(Y) - 1)] for _ in range(len(X) - 1)]

    for rect in rectangles:
        x1_idx = sorted_x.index(rect[0])
        x2_idx = sorted_x.index(rect[2]) - 1
        y1_idx = sorted_y.index(rect[1])
        y2_idx = sorted_y.index(rect[3]) - 1
        for i in range(x1_idx, x2_idx + 1):
            for j in range(y1_idx, y2_idx + 1):
                cnt[i][j] = 1

    total_area = 0
    for i in range(len(X) - 1):
        for j in range(len(Y) - 1):
            if cnt[i][j]:
                total_area += (sorted_x[i + 1] - sorted_x[i]) * (sorted_y[j + 1] - sorted_y[j])
                total_area %= mod

    return total_area

## Structure
def rectangleArea(rectangles):
    # Your code here

    pass