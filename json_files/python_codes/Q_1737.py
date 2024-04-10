##Question ID: 1737

def maxDepth(s: str) -> int:
    depth, max_depth = 0, 0
    for ch in s:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        max_depth = max(max_depth, depth)
    return max_depth

## Structure
def maxDepth(s: str) -> int:
    # Your code here

    pass