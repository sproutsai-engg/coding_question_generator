##Question ID: 1318

def minFlips(a: int, b: int, c: int) -> int:
    count = 0
    for i in range(32):
        bitA = (a >> i) & 1
        bitB = (b >> i) & 1
        bitC = (c >> i) & 1
        if bitC == 0:
            count += bitA + bitB
        else:
            count += 1 - (bitA | bitB)
    return count

## Structure
def minFlips(a: int, b: int, c: int) -> int:
    # Your code here

    pass