##Question ID: 967

def minFallingPathSum(matrix):
    n = len(matrix)
    for i in range(1, n):
        for j in range(n):
            min_val = matrix[i - 1][j]
            if j > 0: min_val = min(min_val, matrix[i - 1][j - 1])
            if j < n - 1: min_val = min(min_val, matrix[i - 1][j + 1])
            matrix[i][j] += min_val
    return min(matrix[-1])

## Structure
def minFallingPathSum(matrix):
    # Your code here

    pass