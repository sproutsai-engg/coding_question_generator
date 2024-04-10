##Question ID: 723

def candyCrush(board):
    rows = len(board)
    cols = len(board[0])
    toDo = False
    
    for r in range(rows):
        for c in range(cols - 2):
            val = abs(board[r][c])
            if val and val == abs(board[r][c + 1]) and val == abs(board[r][c + 2]):
                board[r][c] = board[r][c + 1] = board[r][c + 2] = -val
                toDo = True
                
    for r in range(rows - 2):
        for c in range(cols):
            val = abs(board[r][c])
            if val and val == abs(board[r + 1][c]) and val == abs(board[r + 2][c]):
                board[r][c] = board[r + 1][c] = board[r + 2][c] = -val
                toDo = True
                
    for c in range(cols):
        wr = rows - 1
        for r in range(rows - 1, -1, -1):
            if board[r][c] > 0:
                board[wr][c] = board[r][c]
                wr -= 1
                
        for r in range(wr, -1, -1):
            board[r][c] = 0
                
    return candyCrush(board) if toDo else board

## Structure
def candyCrush(board):
    # Your code here

    pass