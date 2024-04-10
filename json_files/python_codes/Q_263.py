##Question ID: 263

def is_ugly(n: int) -> bool:
    if n <= 0:
        return False
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    return n == 1

## Structure
def is_ugly(n: int) -> bool:
    # Your code here

    pass