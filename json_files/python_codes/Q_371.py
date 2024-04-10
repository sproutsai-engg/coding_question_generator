##Question ID: 371

def add(a, b):
    MAX = 0x7FFFFFFF
    MASK = 0xFFFFFFFF
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a <= MAX else ~(a ^ MASK)

## Structure
def add(a, b):
    # Your code here

    pass