##Question ID: 1234

def getMaxSumAndCount(board):
    mod = 1000000007
    n = len(board)
    dp = [[(0, 0) for _ in range(n)] for _ in range(n)]
    dp[n - 1][n - 1] = (0, 1)

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                continue
            currVal = 0 if board[i][j] == 'E' else int(board[i][j])
            up = dp[i - 1][j] if i > 0 else (-1, 0)
            left = dp[i][j - 1] if j > 0 else (-1, 0)
            diag = dp[i - 1][j - 1] if i > 0 and j > 0 else (-1, 0)

            maxTuple = max(up, left, diag)
            if maxTuple[0] == -1:
                continue

            dp[i][j] = (maxTuple[0] + currVal, dp[i][j][1])

            if up == maxTuple:
                dp[i][j] = (dp[i][j][0], (dp[i][j][1] + up[1]) % mod)
            if left == maxTuple:
                dp[i][j] = (dp[i][j][0], (dp[i][j][1] + left[1]) % mod)
            if diag == maxTuple:
                dp[i][j] = (dp[i][j][0], (dp[i][j][1] + diag[1]) % mod)

    return dp[0][0]


## Structure
def getMaxSumAndCount(board):
    # Your code here

    pass