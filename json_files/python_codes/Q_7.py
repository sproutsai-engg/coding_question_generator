##Question ID: 7

def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    res = 0
    while x:
        res = res * 10 + x % 10
        x //= 10
    res *= sign
    return res if -2**31 <= res <= 2**31 - 1 else 0

## Structure
def reverse(x: int) -> int:
    # Your code here

    pass