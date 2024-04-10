##Question ID: 1522

def stoneGameIII(stoneValue):
    n = len(stoneValue)
    dp = [0] * (n + 1)
    dp[n - 1] = stoneValue[n - 1]
    for i in range(n - 2, -1, -1):
        dp[i] = stoneValue[i] - dp[i + 1]
        for j in range(1, 3):
            if i + j < n:
                dp[i] = max(dp[i], stoneValue[i + j] - dp[i + j + 1])
    if dp[0] > 0: return "Alice"
    if dp[0] < 0: return "Bob"
    return "Tie"

## Structure
def stoneGameIII(stoneValue):
    # Your code here

    pass