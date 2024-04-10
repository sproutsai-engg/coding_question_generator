##Question ID: 70

def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b


## Structure
def climbStairs(n):
    # Your code here

    pass