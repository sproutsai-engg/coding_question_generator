##Question ID: 461

def hammingDistance(x: int, y: int) -> int:
    xorResult = x ^ y
    dist = 0
    while xorResult:
        dist += xorResult & 1
        xorResult >>= 1
    return dist

## Structure
def hammingDistance(x: int, y: int) -> int:
    # Your code here

    pass