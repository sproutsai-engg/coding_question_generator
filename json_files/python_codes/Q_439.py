##Question ID: 439

def parseTernary(expression: str) -> str:
    stack = []
    for c in reversed(expression):
        if stack and stack[-1] == '?':
            stack.pop()  # Pop '?'
            first = stack.pop()
            stack.pop()  # Pop ':'
            second = stack.pop()
            stack.append(first if c == 'T' else second)
        else:
            stack.append(c)
    return stack[-1]


## Structure
def parseTernary(expression: str) -> str:
    # Your code here

    pass