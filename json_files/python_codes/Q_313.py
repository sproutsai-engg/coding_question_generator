##Question ID: 313

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    indices = [0] * len(primes)

    for i in range(1, n):
        min_val = float("inf")

        for j in range(len(primes)):
            min_val = min(min_val, ugly[indices[j]] * primes[j])

        ugly[i] = min_val

        for j in range(len(primes)):
            if ugly[i] == ugly[indices[j]] * primes[j]:
                indices[j] += 1

    return ugly[-1]

## Structure
def nthSuperUglyNumber(n, primes):
    # Your code here

    pass