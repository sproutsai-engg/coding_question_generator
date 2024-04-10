##Question ID: 343

def integer_break(n):
    if n <= 3:
        return n - 1
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    return product * n

## Structure
def integer_break(n):
    # Your code here

    pass