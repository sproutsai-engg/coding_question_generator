##Question ID: 730

def countPalindromicSubsequences(s: str) -> int:
    n = len(s)
    MOD = 1000000007
    dp = [[0] * (n + 1) for _ in range(4)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            c = ord(s[i]) - ord('a')
            dp[c][j] = sum(dp[k][j - 1] for k in range(4)) - dp[c][i] + 2
            dp[c][j] = (dp[c][j] + MOD) % MOD

    return sum(dp[c][n] for c in range(4)) % MOD


## Structure
def countPalindromicSubsequences(s: str) -> int:
    # Your code here

    pass