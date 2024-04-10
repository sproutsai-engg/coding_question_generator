##Question ID: 874

def backspace_compare(s, t):
    def process_backspaces(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack

    return process_backspaces(s) == process_backspaces(t)

## Structure
def backspace_compare(s, t):
    # Your code here

    pass