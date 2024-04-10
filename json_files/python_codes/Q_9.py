##Question ID: 9

def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    original, reversed = x, 0
    while x > 0:
        reversed = reversed * 10 + x % 10
        x //= 10
    return original == reversed


## Structure
def is_palindrome(x: int) -> bool:
    # Your code here

    pass