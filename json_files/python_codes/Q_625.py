##Question ID: 625

def smallestFactorization(num: int) -> int:
    if num == 1:
        return 1
    result = 0
    factor = 1
    for i in range(9, 1, -1):
        while num % i == 0:
            num //= i
            result += i * factor
            factor *= 10
            if result > 2**31 - 1:
                return 0
    return result if num == 1 else 0

## Structure
def smallestFactorization(num: int) -> int:
    # Your code here

    pass