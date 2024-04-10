##Question ID: 798

def moves_to_chessboard(board):
    N = len(board)
    row, col = 0, 0
    row_count, col_count = 0, 0

    for i in range(N):
        for j in range(N):
            if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0:
                return -1

    for i in range(N):
        row ^= board[0][i]
        col ^= board[i][0]
        row_count += 1 if board[0][i] == 1 else 0
        col_count += 1 if board[i][0] == 1 else 0

    if row != 0 and row_count * 2 != N:
        return -1
    if col != 0 and col_count * 2 != N:
        return -1

    if N % 2 == 1:
        if row_count % 2 == 1:
            row_count = N - row_count
        if col_count % 2 == 1:
            col_count = N - col_count
    else:
        row_count = min(row_count, N - row_count)
        col_count = min(col_count, N - col_count)

    return (row_count + col_count) // 2

## Structure
def moves_to_chessboard(board):
    # Your code here

    pass