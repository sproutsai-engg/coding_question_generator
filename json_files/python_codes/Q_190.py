##Question ID: 190

def reverse_bits(n: int) -> int:
    res = 0
    for _ in range(32):
        res <<= 1
        res |= n & 1
        n >>= 1
    return res

## Structure
def reverse_bits(n: int) -> int:
    # Your code here

    pass