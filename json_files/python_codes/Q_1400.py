##Question ID: 1400

def tictactoe(moves):
    grid = [[0] * 3 for _ in range(3)]
    player = 1
    for move in moves:
        r, c = move
        grid[r][c] = player
        if (all(grid[i][c] == player for i in range(3)) or
            all(grid[r][i] == player for i in range(3)) or
            (r == c and all(grid[i][i] == player for i in range(3))) or
            (r + c == 2 and all(grid[i][2 - i] == player for i in range(3)))):
            return 'A' if player == 1 else 'B'
        player = 3 - player
    
    return 'Draw' if len(moves) == 9 else 'Pending'


## Structure
def tictactoe(moves):
    # Your code here

    pass