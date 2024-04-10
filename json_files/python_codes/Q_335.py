##Question ID: 335

def is_path_crossing(distance):
    visited = set([(0, 0)])
    x, y = 0, 0
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
    for i, d in enumerate(distance):
        dx, dy = directions[i % 4]
        for _ in range(d):
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
    return False


## Structure
def is_path_crossing(distance):
    # Your code here

    pass