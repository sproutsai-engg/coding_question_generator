##Question ID: 1756

def min_deletions(s: str) -> int:
    a_count, deletions = 0, 0
    for c in s:
        if c == 'a':
            a_count += 1
        else:
            if a_count > 0:
                a_count -= 1
            else:
                deletions += 1
    return deletions

## Structure
def min_deletions(s: str) -> int:
    # Your code here

    pass