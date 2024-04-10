##Question ID: 810

def valid_tic_tac_toe(board: List[str]) -> bool:
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    if x_count != o_count and x_count != o_count + 1: return False

    x_win, o_win = False, False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            x_win, o_win = (True, o_win) if board[i][0] == 'X' else (x_win, True)
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            x_win, o_win = (True, o_win) if board[0][i] == 'X' else (x_win, True)
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        x_win, o_win = (True, o_win) if board[0][0] == 'X' else (x_win, True)
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        x_win, o_win = (True, o_win) if board[0][2] == 'X' else (x_win, True)

    if x_win and o_win: return False
    if x_win and x_count == o_count: return False
    if o_win and x_count > o_count: return False

    return True


## Structure
def valid_tic_tac_toe(board: List[str]) -> bool:
    # Your code here

    pass