##Question ID: 1457

def minDifficulty(jobDifficulty, d):
    n = len(jobDifficulty)
    if n < d: return -1
    dp = [[float("inf")] * n for _ in range(d)]

    dp[0][0] = jobDifficulty[0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], jobDifficulty[i])

    for i in range(1, d):
        for j in range(i, n):
            maxD = jobDifficulty[j]
            for k in range(j, i - 1, -1):
                maxD = max(maxD, jobDifficulty[k])
                dp[i][j] = min(dp[i][j], dp[i-1][k-1] + maxD)

    return dp[d-1][n-1]


## Structure
def minDifficulty(jobDifficulty, d):
    # Your code here

    pass