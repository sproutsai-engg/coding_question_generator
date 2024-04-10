##Question ID: 1276

def closest_factors(num):
    factor1 = int((num + 2) ** 0.5)
    while True:
        factor2 = (num + 2) // factor1
        if factor1 * factor2 == num + 2:
            return factor1, factor2
        factor2 = (num + 1) // factor1
        if factor1 * factor2 == num + 1:
            return factor1, factor2
        factor1 -= 1

## Structure
def closest_factors(num):
    # Your code here

    pass