##Question ID: 1078

def remove_outer_parentheses(s: str) -> str:
    result = []
    opened = 0

    for c in s:
        if c == '(':
            if opened > 0:
                result.append(c)
            opened += 1
        elif c == ')':
            if opened > 1:
                result.append(c)
            opened -= 1

    return ''.join(result)


## Structure
def remove_outer_parentheses(s: str) -> str:
    # Your code here

    pass