##Question ID: 1871

def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def check_partitioning(s):
    n = len(s)
    for i in range(n - 2):
        if is_palindrome(s, 0, i):
            for j in range(i + 1, n - 1):
                if is_palindrome(s, i + 1, j) and is_palindrome(s, j + 1, n - 1):
                    return True
    return False


## Structure
def is_palindrome(s, l, r):
    # Your code here

    pass