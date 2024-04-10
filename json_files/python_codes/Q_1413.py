##Question ID: 1413

def maxSideLength(mat, threshold):
    m, n = len(mat), len(mat[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    ans = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = mat[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
            k = ans + 1
            if i >= k and j >= k and dp[i][j] - dp[i][j - k] - dp[i - k][j] + dp[i - k][j - k] <= threshold:
                ans += 1

    return ans

## Structure
def maxSideLength(mat, threshold):
    # Your code here

    pass