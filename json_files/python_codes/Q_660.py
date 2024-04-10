##Question ID: 660

def newInteger(n):
    result = 0
    base = 1
    while n:
        result += n % 9 * base
        n //= 9
        base *= 10
    return result

## Structure
def newInteger(n):
    # Your code here

    pass