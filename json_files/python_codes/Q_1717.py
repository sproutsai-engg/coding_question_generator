##Question ID: 1717

def min_cost(cost, size1, size2):
    dp = [float('inf')] * (size2 + 1)
    dp[0] = 0

    for i in range(size1):
        for j in range(size2, -1, -1):
            min_cost = float('inf')
            for k in range(size2):
                if (1 << k) & j == 0:
                    min_cost = min(min_cost, cost[i][k] + dp[j | (1 << k)])
            dp[j] = min(dp[j], min_cost)

    return dp[(1 << size2) - 1]

## Structure
def min_cost(cost, size1, size2):
    # Your code here

    pass