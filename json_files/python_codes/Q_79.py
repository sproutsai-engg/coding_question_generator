##Question ID: 79

def exist(board, word):
    m, n = len(board), len(board[0])

    def dfs(i, j, k):
        if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        tmp, board[i][j] = board[i][j], '/'
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = tmp
        return res

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False


## Structure
def exist(board, word):
    # Your code here

    pass