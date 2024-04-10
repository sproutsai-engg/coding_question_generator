##Question ID: 1042

def mergeStones(stones, k):
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1
    prefixSum = [0] * (n + 1)
    dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        prefixSum[i + 1] = prefixSum[i] + stones[i]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for m in range(2, k + 1):
                for p in range(i, j + 1 - m + 1, k - 1):
                    dp[i][j][m] = (dp[i][p][1] + dp[p + 1][j][m - 1]) % (1e9 + 7)
            if (j - i) % (k - 1) == 0:
                dp[i][j][1] = (dp[i][j][k] + prefixSum[j + 1] - prefixSum[i]) % (1e9 + 7)

    return dp[0][n - 1][1]

## Structure
def mergeStones(stones, k):
    # Your code here

    pass