##Question ID: 672

def num_light_configuration(n, presses):
    dp = [[0] * (presses + 1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(n + 1):
        for j in range(1, presses + 1):
            dp[i][j] = dp[i][j - 1] * (i + 1) + (dp[i - 1][j - 1] if i > 0 else 0)

    return dp[n][presses]

## Structure
def num_light_configuration(n, presses):
    # Your code here

    pass