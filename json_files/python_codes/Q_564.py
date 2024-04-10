##Question ID: 564

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def closest_palindrome(n: str) -> int:
    num = int(n)
    left = num - 1
    right = num + 1

    while True:
        if is_palindrome(str(left)):
            return left
        if is_palindrome(str(right)):
            return right
        left -= 1
        right += 1

## Structure
def is_palindrome(s: str) -> bool:
    # Your code here

    pass