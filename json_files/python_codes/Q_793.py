##Question ID: 793

def canTransform(start: str, end: str) -> bool:
    if len(start) != len(end): return False

    i, j = 0, 0
    n = len(start)
    while i < n and j < n:
        while i < n and start[i] == 'X': i += 1
        while j < n and end[j] == 'X': j += 1

        if start[i] != end[j]: return False

        if (start[i] == 'R' and i > j) or (start[i] == 'L' and i < j): return False

        i += 1; j += 1
    return True

## Structure
def canTransform(start: str, end: str) -> bool:
    # Your code here

    pass