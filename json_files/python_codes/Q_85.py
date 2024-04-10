##Question ID: 85

def maximalRectangle(matrix):
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    height = [0] * (n + 1)
    max_area = 0

    for i in range(m):
        s = []
        for j in range(n + 1):
            if j < n:
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0
            while s and height[j] < height[s[-1]]:
                h = height[s.pop()]
                w = j if not s else j - s[-1] - 1
                max_area = max(max_area, h * w)
            s.append(j)

    return max_area


## Structure
def maximalRectangle(matrix):
    # Your code here

    pass