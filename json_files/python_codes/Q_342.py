##Question ID: 342

def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1

## Structure
def isPowerOfFour(n: int) -> bool:
    # Your code here

    pass