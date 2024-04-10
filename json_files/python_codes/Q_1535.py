##Question ID: 1535

def number_of_ways(n, m, k, mod=1_000_000_007):
    if k > 1:
        result = 1
        for _ in range(n):
            result = (result * m) % mod
        return result
    return 1 if n % 2 == 0 else m

## Structure
def number_of_ways(n, m, k, mod=1_000_000_007):
    # Your code here

    pass