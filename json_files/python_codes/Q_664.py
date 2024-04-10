##Question ID: 664

def strange_printer(s: str) -> int:
    n = len(s)
    if n == 0: return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for len in range(1, n):
        for i in range(n - len):
            j = i + len
            dp[i][j] = dp[i+1][j] + 1
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
    return dp[0][n-1]

## Structure
def strange_printer(s: str) -> int:
    # Your code here

    pass