##Question ID: 767

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_set_bits(left: int, right: int) -> int:
    count = 0
    for i in range(left, right + 1):
        bits = bin(i).count('1')
        if is_prime(bits):
            count += 1
    return count

## Structure
def is_prime(n: int) -> bool:
    # Your code here

    pass