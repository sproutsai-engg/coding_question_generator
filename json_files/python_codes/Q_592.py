##Question ID: 592

from fractions import Fraction

def fractionAddition(expression: str) -> str:
    fractions = expression.replace('+', ' +').replace('-', ' -').split()
    result = sum(Fraction(fraction) for fraction in fractions)
    return f"{result.numerator}/{result.denominator}"

## Structure
from fractions import Fraction
    # Your code here

    pass