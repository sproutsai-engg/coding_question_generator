##Question ID: 1719

def check_ways(pairs):
    candidates = {}
    for x, y in pairs:
        candidates[x] = candidates.get(x, 0) + 1
        candidates[y] = candidates.get(y, 0) + 1

    root_count = sum(1 for v in candidates.values() if v == 1)
    return min(root_count, 2)

## Structure
def check_ways(pairs):
    # Your code here

    pass