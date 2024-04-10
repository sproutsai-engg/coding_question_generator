##Question ID: 1426

def sum_zero(n):
    res = []
    for i in range(1, (n // 2) + 1):
        res.append(i)
        res.append(-i)
    if n % 2 != 0:
        res.append(0)
    return res

## Structure
def sum_zero(n):
    # Your code here

    pass