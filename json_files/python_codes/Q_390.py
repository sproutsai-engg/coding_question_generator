##Question ID: 390

def last_remaining(n: int) -> int:
    direction = True
    head = 1
    remaining = n
    step = 1

    while remaining > 1:
        if direction or remaining % 2 == 1:
            head += step
        remaining //= 2
        step *= 2
        direction = not direction

    return head

## Structure
def last_remaining(n: int) -> int:
    # Your code here

    pass