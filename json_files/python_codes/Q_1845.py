##Question ID: 1845

def largestSubmatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    height = [0] * n
    max_area = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0
        sorted_height = sorted(height)
        for j in range(n):
            max_area = max(max_area, sorted_height[j] * (n - j))

    return max_area


## Structure
def largestSubmatrix(matrix):
    # Your code here

    pass