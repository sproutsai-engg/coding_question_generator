##Question ID: 1808

def stoneGame(stones):
    n = len(stones)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(stones[j] - dp[i][j - 1], stones[i] - dp[i + 1][j])
    
    return dp[0][n - 1]

## Structure
def stoneGame(stones):
    # Your code here

    pass