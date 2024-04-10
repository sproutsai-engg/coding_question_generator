##Question ID: 1406

def stoneGameIII(stoneValue):
    n = len(stoneValue)
    dp = [float("-inf")] * (n + 1)
    dp[n] = 0
    
    for i in range(n - 1, -1, -1):
        curr = 0
        for j in range(3):
            if i + j < n:
                curr += stoneValue[i + j]
                dp[i] = max(dp[i], curr - dp[i + j + 1])
                
    return "Tie " if dp[0] == 0 else "Alice " if dp[0] > 0 else "Bob "


## Structure
def stoneGameIII(stoneValue):
    # Your code here

    pass