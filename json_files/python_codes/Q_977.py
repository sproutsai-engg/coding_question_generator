##Question ID: 977

def distinctSubseqII(s):
    mod = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    last = [-1] * 26

    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * 2) % mod
        if last[ord(s[i - 1]) - ord('a')] != -1:
            dp[i] = (dp[i] - dp[last[ord(s[i - 1]) - ord('a')]] + mod) % mod
        last[ord(s[i - 1]) - ord('a')] = i - 1

    dp[n] = (dp[n] - 1 + mod) % mod
    return dp[n]

## Structure
def distinctSubseqII(s):
    # Your code here

    pass