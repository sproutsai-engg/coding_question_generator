##Question ID: 1317

def no_zero_integers(n: int):
    for a in range(1, n):
        if '0' not in str(a) and '0' not in str(n - a):
            return [a, n - a]
    return [0, 0]  # never gets here

## Structure
def no_zero_integers(n: int):
    # Your code here

    pass