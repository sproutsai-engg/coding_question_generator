##Question ID: 1259

def numberOfWays(numPeople: int) -> int:
    MOD = 1000000007
    dp = [0] * (numPeople // 2 + 1)
    dp[0] = 1
    for i in range(1, numPeople // 2 + 1):
        for j in range(1, i + 1):
            dp[i] = (dp[i] + dp[i - j] * dp[j - 1]) % MOD
    return dp[numPeople // 2]


## Structure
def numberOfWays(numPeople: int) -> int:
    # Your code here

    pass