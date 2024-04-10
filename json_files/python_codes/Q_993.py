##Question ID: 993

def tallestBillboard(rods):
    n = len(rods)
    totalLength = sum(rods)
    dp = [[-1] * (totalLength + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(totalLength + 1):
            dp[i][j] = dp[i - 1][j]
            if rods[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - rods[i - 1]] + rods[i - 1])
            if rods[i - 1] <= totalLength - j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j + rods[i - 1]])
                
    return dp[n][0] // 2


## Structure
def tallestBillboard(rods):
    # Your code here

    pass