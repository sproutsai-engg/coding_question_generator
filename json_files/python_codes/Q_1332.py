##Question ID: 1332

def countStrings(n):
    mod = 10**9 + 7
    a, b = 1, 1
    for _ in range(n):
        a = (a * 2) % mod
        b = (b * 3) % mod
    return (b - a + mod) % mod


## Structure
def countStrings(n):
    # Your code here

    pass