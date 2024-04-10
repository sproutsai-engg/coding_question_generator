##Question ID: 212

def findWords(board, words):
    def dfs(board, word, index, i, j, visited):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j] or board[i][j] != word[index]:
            return False
        visited[i][j] = True
        found = dfs(board, word, index + 1, i - 1, j, visited) or \
                dfs(board, word, index + 1, i + 1, j, visited) or \
                dfs(board, word, index + 1, i, j - 1, visited) or \
                dfs(board, word, index + 1, i, j + 1, visited)
        visited[i][j] = False
        return found

    res = []
    for word in words:
        if any(dfs(board, word, 0, i, j, [[False] * len(board[0]) for _ in range(len(board))])
               for i in range(len(board)) for j in range(len(board[0]))):
            res.append(word)
    return res


## Structure
def findWords(board, words):
    # Your code here

    pass