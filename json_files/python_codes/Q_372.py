##Question ID: 372

def powmod(a, b):
    if b == 0:
        return 1
    res = powmod(a, b // 2)
    return res * res % 1337 * a % 1337 if b % 2 else res * res % 1337

def superPow(a, b):
    n = 0
    for bi in b:
        n = (n * 10 + bi) % 1140
    return powmod(a % 1337, n + 1140)

## Structure
def powmod(a, b):
    # Your code here

    pass