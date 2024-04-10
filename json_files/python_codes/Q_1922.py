##Question ID: 1922

def goodDigitStrings(n: int) -> int:
    MOD = 1000000007
    even_count, prime_count = 1, 1
    for i in range(n):
        if i % 2 == 0:
            even_count = (even_count * 5) % MOD
        else:
            prime_count = (prime_count * 4) % MOD
    return (even_count * prime_count) % MOD

## Structure
def goodDigitStrings(n: int) -> int:
    # Your code here

    pass