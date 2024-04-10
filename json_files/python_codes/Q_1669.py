##Question ID: 1669

def minCost(n, cuts):
    cuts = [0] + cuts + [n]
    cuts.sort()
    size = len(cuts)
    dp = [[0] * size for _ in range(size)]

    for len in range(2, size):
        for i in range(size - len):
            j = i + len
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

    return dp[0][size - 1]

## Structure
def minCost(n, cuts):
    # Your code here

    pass