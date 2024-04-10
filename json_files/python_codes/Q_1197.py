##Question ID: 1197

def parse_bool_expr(expression, pos=None):
    if pos is None:
        pos = [0]
    current = expression[pos[0]]
    pos[0] += 1
    if current == 't': return True
    if current == 'f': return False
    if current == '!':
        pos[0] += 1
        return not parse_bool_expr(expression, pos)
    if current == '&':
        pos[0] += 1
        result = True
        while expression[pos[0]] != ')':
            result &= parse_bool_expr(expression, pos)
            if expression[pos[0]] == ',': pos[0] += 1
    elif current == '|':
        pos[0] += 1
        result = False
        while expression[pos[0]] != ')':
            result |= parse_bool_expr(expression, pos)
            if expression[pos[0]] == ',': pos[0] += 1
    pos[0] += 1
    return result

## Structure
def parse_bool_expr(expression, pos=None):
    # Your code here

    pass