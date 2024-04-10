##Question ID: 1837

def sum_base(n: int, k: int) -> int:
    s = 0
    while n:
        s += n % k
        n //= k
    return s


## Structure
def sum_base(n: int, k: int) -> int:
    # Your code here

    pass