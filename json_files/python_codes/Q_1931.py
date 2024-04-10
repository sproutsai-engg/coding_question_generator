##Question ID: 1931

def numOfWays(m, n):
    mod = 1000000007
    a, b, c, d = 6, 6, 3, 3
    while n > 1:
        n -= 1
        temp_a = a
        temp_c = c
        a = (a * 3 + b * 2) % mod
        b = (temp_a * 2 + b * 2) % mod
        c = (c * 3 + d * 2) % mod
        d = (temp_c * 2 + d * 2) % mod
    return b if m == 1 else (a + c) % mod

## Structure
def numOfWays(m, n):
    # Your code here

    pass