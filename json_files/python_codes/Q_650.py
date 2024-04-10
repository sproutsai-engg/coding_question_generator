##Question ID: 650

def min_steps(n):
    result = 0
    i = 2
    while i <= n:
        while n % i == 0:
            result += i
            n //= i
        i += 1
    return result

## Structure
def min_steps(n):
    # Your code here

    pass