##Question ID: 888

def mirrorReflection(p, q):
    from math import gcd
    m = p // gcd(p, q)

    if m % 2 == 0:
        return 2
    if (q // gcd(p, q)) % 2 == 0:
        return 0
    return 1

## Structure
def mirrorReflection(p, q):
    # Your code here

    pass