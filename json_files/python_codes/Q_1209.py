##Question ID: 1209

def removeDuplicates(s: str, k: int) -> str:
    stack = []
    for c in s:
        if not stack or stack[-1][0] != c:
            stack.append((c, 1))
        elif stack[-1][1] + 1 != k:
            stack[-1] = (c, stack[-1][1] + 1)
        else:
            stack.pop()
    return ''.join(c * count for c, count in stack)


## Structure
def removeDuplicates(s: str, k: int) -> str:
    # Your code here

    pass