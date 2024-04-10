##Question ID: 1521

def closestToTarget(arr: List[int], target: int) -> int:
    min_diff = float('inf')
    prefix = set()

    for n in arr:
        next_prefix = set()
        for p in prefix:
            next_prefix.add(p & n)
        next_prefix.add(n)

        for p in next_prefix:
            min_diff = min(min_diff, abs(p - target))
        prefix = next_prefix
    return min_diff

## Structure
def closestToTarget(arr: List[int], target: int) -> int:
    # Your code here

    pass