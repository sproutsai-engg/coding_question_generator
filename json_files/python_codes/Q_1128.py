##Question ID: 1128

def remove_duplicates(s: str) -> str:
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

## Structure
def remove_duplicates(s: str) -> str:
    # Your code here

    pass