##Question ID: 397

def min_operations(n):
    steps = 0
    while n > 1:
        n = n // 2 if n % 2 == 0 else n - 1
        steps += 1
    return steps

## Structure
def min_operations(n):
    # Your code here

    pass