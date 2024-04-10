##Question ID: 843

def numFactoredBinaryTrees(arr):
    MOD = 10**9 + 7
    n = len(arr)
    arr.sort()
    dp = {}
    for i, x in enumerate(arr):
        dp[x] = 1
        for y in arr[:i]:
            if x % y == 0 and x // y in dp:
                dp[x] = (dp[x] + dp[y] * dp[x // y]) % MOD
    return sum(dp.values()) % MOD

## Structure
def numFactoredBinaryTrees(arr):
    # Your code here

    pass