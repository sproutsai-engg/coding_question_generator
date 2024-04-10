##Question ID: 1641

def countVowelStrings(n: int) -> int:
    dp = [1, 1, 1, 1, 1]
    for i in range(2, n + 1):
        for j in range(3, -1, -1):
            dp[j] = dp[j] + dp[j + 1]
    return sum(dp)

## Structure
def countVowelStrings(n: int) -> int:
    # Your code here

    pass