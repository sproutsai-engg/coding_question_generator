##Question ID: 1343

def dieSimulator(n, rollMax):
    MOD = 10**9 + 7
    dp = [[0] * (n + 1) for _ in range(6)]
    sum_dp = [0] * (n + 1)

    for i in range(6):
        dp[i][1] = 1
    sum_dp[1] = 6

    for j in range(2, n + 1):
        cur_sum = 0
        for i in range(6):
            dp[i][j] = sum_dp[j - 1]
            if j - rollMax[i] - 1 >= 0:
                dp[i][j] = (dp[i][j] - sum_dp[j - rollMax[i] - 1] + MOD) % MOD
                if j - rollMax[i] - 1 >= 1:
                    dp[i][j] = (dp[i][j] + dp[i][j - rollMax[i] - 1]) % MOD
            cur_sum = (cur_sum + dp[i][j]) % MOD
        sum_dp[j] = cur_sum

    return sum_dp[n]

## Structure
def dieSimulator(n, rollMax):
    # Your code here

    pass