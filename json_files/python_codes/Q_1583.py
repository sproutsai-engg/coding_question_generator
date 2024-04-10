##Question ID: 1583

def minCost(houses, cost, m, n, target):
    dp = [[[float('inf')] * (target + 1) for _ in range(n)] for _ in range(m)]

    if houses[0] != 0:
        dp[0][houses[0] - 1][1] = 0
    else:
        for j in range(n):
            dp[0][j][1] = cost[0][j]

    for i in range(1, m):
        for j in range(n):
            for k in range(1, target + 1):
                if houses[i] != 0 and houses[i] != j + 1:
                    continue
                paint_cost = 0 if houses[i] != 0 else cost[i][j]

                for l in range(n):
                    if l == j:
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][l][k] + paint_cost)
                    else:
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][l][k - 1] + paint_cost)

    ans = min(dp[m - 1][j][target] for j in range(n))
    return -1 if ans == float('inf') else ans


## Structure
def minCost(houses, cost, m, n, target):
    # Your code here

    pass