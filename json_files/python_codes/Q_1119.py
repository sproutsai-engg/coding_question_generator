##Question ID: 1119

def is_robot_bounded(instructions: str) -> bool:
    x, y, dir = 0, 0, 0
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for c in instructions:
        if c == 'G':
            x += moves[dir][0]
            y += moves[dir][1]
        elif c == 'L':
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4

    return (x == 0 and y == 0) or dir != 0

## Structure
def is_robot_bounded(instructions: str) -> bool:
    # Your code here

    pass