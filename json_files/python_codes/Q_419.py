##Question ID: 419

def countBattleships(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 'X' and
                (i == 0 or board[i - 1][j] == '.') and
                (j == 0 or board[i][j - 1] == '.')):
                count += 1
    return count

## Structure
def countBattleships(board):
    # Your code here

    pass