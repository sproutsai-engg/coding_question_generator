##Question ID: 1134

def is_armstrong(n: int) -> bool:
    power_sum = 0
    original = n
    k = len(str(n))
    while n > 0:
        digit = n % 10
        power_sum += digit ** k
        n //= 10
    return power_sum == original

## Structure
def is_armstrong(n: int) -> bool:
    # Your code here

    pass