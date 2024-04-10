##Question ID: 227

def calculate(s: str) -> int:
    result, num, sign, stack = 0, 0, 1, []

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '+':
            result += sign * num
            num = 0
            sign = 1
        elif c == '-':
            result += sign * num
            num = 0
            sign = -1
        elif c == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif c == ')':
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()
    
    if num:
        result += sign * num
        
    return result

## Structure
def calculate(s: str) -> int:
    # Your code here

    pass