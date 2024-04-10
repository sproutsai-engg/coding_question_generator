##Question ID: 22

def generate_parenthesis(n):
    def generate_parenthesis_helper(open, close, current):
        if open == 0 and close == 0:
            result.append(current)
            return
        if open > 0:
            generate_parenthesis_helper(open - 1, close + 1, current + '(')
        if close > 0:
            generate_parenthesis_helper(open, close - 1, current + ')')

    result = []
    generate_parenthesis_helper(n, 0, '')
    return result


## Structure
def generate_parenthesis(n):
    # Your code here

    pass