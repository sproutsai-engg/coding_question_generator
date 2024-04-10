##Question ID: 241

def diffWaysToCompute(input: str):
    result = []
    for i in range(len(input)):
        c = input[i]
        if c == '+' or c == '-' or c == '*':
            left = diffWaysToCompute(input[:i])
            right = diffWaysToCompute(input[i + 1:])
            for l in left:
                for r in right:
                    if c == '+': result.append(l + r)
                    elif c == '-': result.append(l - r)
                    elif c == '*': result.append(l * r)
    if not result:
        result.append(int(input))
    return result

## Structure
def diffWaysToCompute(input: str):
    # Your code here

    pass