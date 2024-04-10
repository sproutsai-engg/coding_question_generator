##Question ID: 1041

def numRookCaptures(board):
    x, y, captures = 0, 0, 0

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                x, y = i, j
                break
        if board[x][y] == 'R':
            break

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8:
            if board[nx][ny] == 'p':
                captures += 1
                break
            elif board[nx][ny] == 'B':
                break
            nx += dx
            ny += dy

    return captures


## Structure
def numRookCaptures(board):
    # Your code here

    pass