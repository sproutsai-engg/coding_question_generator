##Question ID: 202

def get_next(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit * digit
        n //= 10
    return sum

def is_happy(n):
    slow, fast = n, get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1

## Structure
def get_next(n):
    # Your code here

    pass