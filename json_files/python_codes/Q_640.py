##Question ID: 640

def solve_equation(equation: str) -> str:
    coef = val = left = operate = 0
    equation += '+'
    parts = [s.strip()+c for c in equation if c in '+-' for s in equation.split(c)]
    for part in parts:
        if part == '=':
            left = -1
            operate = 1
        else:
            n, x = part.split('x')
            value_to_change = 1 if n else int(n)
            if x:
                coef += (1 if part[0] == '+' else -1) * left * operate * value_to_change
            else:
                val += (1 if part[0] == '+' else -1) * left * operate * value_to_change
            operate = 1 - x.find('x')

    if coef == 0:
        return "Infinite solutions" if val == 0 else "No solution"
    return "x=" + str(-val // coef)


## Structure
def solve_equation(equation: str) -> str:
    # Your code here

    pass