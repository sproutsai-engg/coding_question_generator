##Question ID: 50

def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    currentProduct = x
    i = n
    while i:
        if i % 2 == 1:
            result *= currentProduct
        currentProduct *= currentProduct
        i //= 2
    return result

## Structure
def myPow(x: float, n: int) -> float:
    # Your code here

    pass