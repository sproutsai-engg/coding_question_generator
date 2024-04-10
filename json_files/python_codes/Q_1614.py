##Question ID: 1614

def maxDepth(s: str) -> int:
    depth = 0
    max_depth = 0

    for c in s:
        if c == '(':
            depth += 1
            max_depth = max(depth, max_depth)
        elif c == ')':
            depth -= 1

    return max_depth

## Structure
def maxDepth(s: str) -> int:
    # Your code here

    pass