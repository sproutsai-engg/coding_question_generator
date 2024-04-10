##Question ID: 1175

def numPrimeArrangements(n: int) -> int:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
    composite_count = n - prime_count

    MOD = 10**9 + 7
    res = 1
    for i in range(1, prime_count + 1):
        res = res * i % MOD
    for i in range(1, composite_count + 1):
        res = res * i % MOD

    return res

## Structure
def numPrimeArrangements(n: int) -> int:
    # Your code here

    pass