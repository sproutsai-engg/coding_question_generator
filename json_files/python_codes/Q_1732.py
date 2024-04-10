##Question ID: 1732

def min_operations(n):
    operations = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        operations += 1
    return operations

## Structure
def min_operations(n):
    # Your code here

    pass