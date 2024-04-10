##Question ID: 1416

def numDecodings(s: str, k: int) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1
    MOD = 1000000007

    for i in range(n - 1, -1, -1):
        num = 0
        for j in range(i, n):
            num = num * 10 + int(s[j])
            if num >= 1 and num <= k:
                dp[i] = (dp[i] + dp[j + 1]) % MOD
            if num > k:
                break

    return dp[0]

## Structure
def numDecodings(s: str, k: int) -> int:
    # Your code here

    pass