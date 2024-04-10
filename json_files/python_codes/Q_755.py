##Question ID: 755

def min_moves(target: int) -> int:
    target = abs(target)
    step = 0
    total = 0
    while total < target or (total - target) % 2 != 0:
        step += 1
        total += step
    return step


## Structure
def min_moves(target: int) -> int:
    # Your code here

    pass