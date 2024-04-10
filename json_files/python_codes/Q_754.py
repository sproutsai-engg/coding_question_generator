##Question ID: 754

def reachNumber(target: int) -> int:
    target = abs(target)
    step = 0
    sum = 0
    while sum < target:
        step += 1
        sum += step
    while (sum - target) % 2 != 0:
        step += 1
        sum += step
    return step


## Structure
def reachNumber(target: int) -> int:
    # Your code here

    pass