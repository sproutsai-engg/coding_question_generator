##Question ID: 91

def numDecodings(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, n + 1):
        one_digit = int(s[i - 1:i])
        two_digits = int(s[i - 2:i])

        if one_digit >= 1:
            dp[i] += dp[i - 1]
        if two_digits >= 10 and two_digits <= 26:
            dp[i] += dp[i - 2]
    return dp[n]


## Structure
def numDecodings(s: str) -> int:
    # Your code here

    pass