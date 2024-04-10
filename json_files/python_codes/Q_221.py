##Question ID: 221

def maximalSquare(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maxSize = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxSize = max(maxSize, dp[i][j])

    return maxSize * maxSize

## Structure
def maximalSquare(matrix):
    # Your code here

    pass