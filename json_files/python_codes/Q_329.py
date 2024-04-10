##Question ID: 329

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(matrix, memo, i, j):
    if memo[i][j] != 0:
        return memo[i][j]
    
    max_len = 0
    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if (0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] > matrix[i][j]):
            max_len = max(max_len, dfs(matrix, memo, ni, nj))
    
    memo[i][j] = max_len + 1
    return memo[i][j]

def longest_increasing_path(matrix):
    m, n = len(matrix), len(matrix[0])
    
    memo = [[0] * n for _ in range(m)]
    
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(matrix, memo, i, j))
    
    return ans


## Structure
dx = (0, 0, 1, -1)
    # Your code here

    pass