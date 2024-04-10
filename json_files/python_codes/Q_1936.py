##Question ID: 1936

def numberOfNiceDivisors(primeFactors):
    MOD = 1000000007
    result = 1
    p = 2
    while p <= primeFactors:
        if primeFactors % p == 0:
            count = 0
            while primeFactors % p == 0:
                primeFactors //= p
                count += 1
            result = (result * (count * 2 + 1)) % MOD
        p += 1
    return result

## Structure
def numberOfNiceDivisors(primeFactors):
    # Your code here

    pass