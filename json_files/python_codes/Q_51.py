##Question ID: 51

def solveNQueens(n):
    def isSafe(board, row, col):
        for i in range(col):
            if board[row][i] == 'Q': return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q': return False
            i, j = i - 1, j - 1
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 'Q': return False
            i, j = i + 1, j - 1
        return True

    def solve(result, board, n, col):
        if col == n:
            result.append(board.copy())
            return
        for row in range(n):
            if isSafe(board, row, col):
                board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                solve(result, board, n, col + 1)
                board[row] = board[row][:col] + '.' + board[row][col + 1:]

    result, board = [], ['.' * n for _ in range(n)]
    solve(result, board, n, 0)
    return result

## Structure
def solveNQueens(n):
    # Your code here

    pass