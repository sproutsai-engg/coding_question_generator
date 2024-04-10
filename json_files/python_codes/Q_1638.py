##Question ID: 1638

def get_min_dist_sum(positions: List[List[int]]) -> float:
    x, y = 0, 0
    n = len(positions)
    for pos in positions:
        x += pos[0]
        y += pos[1]
    x /= n
    y /= n
    return x

## Structure
def get_min_dist_sum(positions: List[List[int]]) -> float:
    # Your code here

    pass