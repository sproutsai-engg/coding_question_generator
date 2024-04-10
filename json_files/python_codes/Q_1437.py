##Question ID: 1437

def min_steps_to_make_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

## Structure
def min_steps_to_make_palindrome(s):
    # Your code here

    pass