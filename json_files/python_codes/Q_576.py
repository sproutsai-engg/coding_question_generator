##Question ID: 576

def findPaths(m, n, maxMove, startRow, startColumn):               
    MOD = 10**9 + 7                     
    dp = [[[0]* n for _ in range(m)] for _ in range(maxMove + 1)]
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for k in range(1, maxMove + 1):                                
        for i in range(m):                                         
            for j in range(n):                                           
                for move in moves:              
                    ni, nj = i + move[0], j + move[1]
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:                                 
                        dp[k][i][j] = (dp[k][i][j] + 1) % MOD          
                    else:
                        dp[k][i][j] = (dp[k][i][j] + dp[k - 1][ni][nj]) % MOD

    return dp[maxMove][startRow][startColumn]

## Structure
def findPaths(m, n, maxMove, startRow, startColumn):               
    # Your code here

    pass