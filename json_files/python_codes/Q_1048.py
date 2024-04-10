##Question ID: 1048

def clumsy(n: int) -> int:
    if n <= 2:
        return n
    if n == 3:
        return 6
    result = n * (n - 1) // (n - 2) + (n - 3)
    n -= 4
    while n >= 4:
        result = result - (n * (n - 1) // (n - 2)) + (n - 3)
        n -= 4
    return result - clumsy(n)


## Structure
def clumsy(n: int) -> int:
    # Your code here

    pass