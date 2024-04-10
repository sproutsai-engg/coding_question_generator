##Question ID: 474

def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for s in strs:
        ones = s.count('1')
        zeros = len(s) - ones
        
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    
    return dp[m][n]

## Structure
def findMaxForm(strs, m, n):
    # Your code here

    pass