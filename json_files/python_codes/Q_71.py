##Question ID: 71

def simplifyPath(path: str) -> str:
    stack = []
    parts = path.split("/")

    for part in parts:
        if not part or part == ".":
            continue
        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)

## Structure
def simplifyPath(path: str) -> str:
    # Your code here

    pass