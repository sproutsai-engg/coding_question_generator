##Question ID: 657

def judgeCircle(moves: str) -> bool:
    x, y = 0, 0
    for move in moves:
        if move == 'U': y += 1
        elif move == 'D': y -= 1
        elif move == 'R': x += 1
        elif move == 'L': x -= 1
    return x == 0 and y == 0

## Structure
def judgeCircle(moves: str) -> bool:
    # Your code here

    pass