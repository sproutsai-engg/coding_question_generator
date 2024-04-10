##Question ID: 1320

def removeDuplicates(s: str, k: int) -> str:
    stack = []
    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])
    return ''.join(c * n for c, n in stack)

## Structure
def removeDuplicates(s: str, k: int) -> str:
    # Your code here

    pass