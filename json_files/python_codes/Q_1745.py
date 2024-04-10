##Question ID: 1745

def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def check_partitioning(s):
    n = len(s)
    for i in range(0, n - 2):
        if is_palindrome(s, 0, i):
            for j in range(i + 1, n - 1):
                if is_palindrome(s, i + 1, j) and is_palindrome(s, j + 1, n - 1):
                    return True
    return False

## Structure
def is_palindrome(s, start, end):
    # Your code here

    pass