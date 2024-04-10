##Question ID: 598

def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
    for op in ops:
        m = min(m, op[0])
        n = min(n, op[1])
    return m * n

## Structure
def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
    # Your code here

    pass