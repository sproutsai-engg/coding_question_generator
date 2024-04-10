##Question ID: 201

def range_bitwise_and(left: int, right: int) -> int:
    shift = 0
    while left != right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift

## Structure
def range_bitwise_and(left: int, right: int) -> int:
    # Your code here

    pass