##Question ID: 1371

def min_remove_to_make_valid(s: str) -> str:
    stk = []
    result = list(s)

    for i, ch in enumerate(s):
        if ch == '(':
            stk.append(i)
        elif ch == ')':
            if stk:
                stk.pop()
            else:
                result[i] = ''

    for i in stk:
        result[i] = ''

    return ''.join(result)


## Structure
def min_remove_to_make_valid(s: str) -> str:
    # Your code here

    pass