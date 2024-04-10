##Question ID: 1111

def minScoreTriangulation(values):
    n = len(values)
    dp = [[0] * n for _ in range(n)]

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], values[i] * values[j] * values[k] + dp[i][k] + dp[k][j])

    return dp[0][n - 1]


## Structure
def minScoreTriangulation(values):
    # Your code here

    pass