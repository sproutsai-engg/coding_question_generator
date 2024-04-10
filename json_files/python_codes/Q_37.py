##Question ID: 37

def isValid(board, row, col, c):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
            return False
    return True

def solveSudokuHelper(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for c in '123456789':
                    if isValid(board, i, j, c):
                        board[i][j] = c

                        if solveSudokuHelper(board):
                            return True

                        board[i][j] = '.'
                return False

    return True

def solveSudoku(board):
    solveSudokuHelper(board)

## Structure
def isValid(board, row, col, c):
    # Your code here

    pass