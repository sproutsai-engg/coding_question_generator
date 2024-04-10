##Question ID: 911

def profitableSchemes(n, minProfit, group, profit):
    dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
    mod = 10**9 + 7
    dp[0][0] = 1
    for i in range(len(group)):
        for j in range(n, group[i] - 1, -1):
            for k in range(minProfit, -1, -1):
                dp[j][k] = (dp[j][k] + dp[j - group[i]][max(0, k - profit[i])]) % mod
    return sum(dp[i][minProfit] for i in range(1, n + 1)) % mod

## Structure
def profitableSchemes(n, minProfit, group, profit):
    # Your code here

    pass