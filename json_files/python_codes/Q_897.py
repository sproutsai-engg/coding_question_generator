##Question ID: 897

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def prime_palindrome(n):
    while True:
        if is_prime(n) and is_palindrome(n):
            return n
        n += 1

## Structure
def is_prime(n):
    # Your code here

    pass