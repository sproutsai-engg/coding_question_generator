##Question ID: 132

def minCut(s):
    n = len(s)
    dp = [i - 1 for i in range(n + 1)]
    is_palindrome = [[False] * n for _ in range(n)]
    
    for j in range(1, n):
        for i in range(j, -1, -1):
            if s[i] == s[j] and (j - i < 2 or is_palindrome[i + 1][j - 1]):
                is_palindrome[i][j] = True
                dp[j + 1] = min(dp[j + 1], dp[i] + 1)
                
    return dp[n]

## Structure
def minCut(s):
    # Your code here

    pass