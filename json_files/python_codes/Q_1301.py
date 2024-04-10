##Question ID: 1301

from typing import List

MOD = 10**9 + 7

def pathsWithMaxScore(board: List[str]) -> List[int]:
    n = len(board)
    dp = [[0] * n for _ in range(n)]
    cnt = [[0] * n for _ in range(n)]

    board[0] = list(board[0])
    board[0][0] = '0'
    board[n-1] = list(board[n-1])
    board[n-1][n-1] = '0'
    cnt[n-1][n-1] = 1

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if board[i][j] != 'X':
                neighbors = [(i-1, j), (i, j-1), (i-1, j-1)]
                for x, y in neighbors:
                    if x >= 0 and y >= 0:
                        if dp[i][j] < dp[x][y] + int(board[i][j]):
                            dp[i][j] = dp[x][y] + int(board[i][j])
                            cnt[i][j] = cnt[x][y]
                        elif dp[i][j] == dp[x][y] + int(board[i][j]):
                            cnt[i][j] = (cnt[i][j] + cnt[x][y]) % MOD

    return [dp[0][0], cnt[0][0]]


## Structure
from typing import List
    # Your code here

    pass