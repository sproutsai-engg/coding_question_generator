##Question ID: 1278

def palindromePartition(s: str, k: int) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for len in range(2, n + 1):
        for i in range(n - len + 1):
            j = i + len - 1
            dp[i][j] = dp[i + 1][j - 1] + (s[i] != s[j])

    memo = [float('inf')] * n
    for i in range(n):
        if dp[0][i] == 0:
            memo[i] = 0
        else:
            for j in range(i):
                memo[i] = min(memo[i], memo[j] + dp[j + 1][i])

    return memo[-1] + k



## Structure
def palindromePartition(s: str, k: int) -> int:
    # Your code here

    pass