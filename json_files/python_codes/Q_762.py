##Question ID: 762

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_set_bits(left: int, right: int) -> int:
    return sum(is_prime(bin(i).count('1')) for i in range(left, right + 1))


## Structure
def is_prime(n: int) -> bool:
    # Your code here

    pass