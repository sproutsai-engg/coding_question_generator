##Question ID: 1619

def is_path_crossing(path: str) -> bool:
    visited = {(0, 0)}
    x, y = 0, 0
    for dir in path:
        if dir == 'N': y += 1
        elif dir == 'S': y -= 1
        elif dir == 'E': x += 1
        elif dir == 'W': x -= 1
        if (x, y) in visited: return True
        visited.add((x, y))
    return False

## Structure
def is_path_crossing(path: str) -> bool:
    # Your code here

    pass