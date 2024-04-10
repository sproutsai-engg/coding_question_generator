##Question ID: 1190

def reverseParentheses(s: str) -> str:
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            start, end = stack.pop(), i
            # reversal of the substring
            s = s[:start] + s[start+1:end][::-1] + s[end+1:]
    return ''.join(c for c in s if c.isalpha())

## Structure
def reverseParentheses(s: str) -> str:
    # Your code here

    pass