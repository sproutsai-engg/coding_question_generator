##Question ID: 1639

def numWays(words, target):
    n = len(words)
    m = len(target)
    count = [[0] * 26 for _ in range(n)]
    dp = [[0] * n for _ in range(m)]
    mod = 1000000007

    for i, word in enumerate(words):
        for c in word:
            count[i][ord(c) - ord('a')] += 1

    for i in range(n):
        dp[0][i] = count[i][ord(target[0]) - ord('a')]

    for i in range(1, m):
        for j in range(n):
            for k in range(n):
                dp[i][j] = (dp[i][j] + dp[i-1][k] * count[j][ord(target[i]) - ord('a')]) % mod

    return sum(dp[m-1]) % mod

## Structure
def numWays(words, target):
    # Your code here

    pass