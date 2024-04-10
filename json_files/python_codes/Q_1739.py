##Question ID: 1739

def check_palindrome_formation(a: str, b: str) -> bool:
    def is_palindrome(s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    i, j = 0, len(a) - 1
    while i < j:
        if a[i] != b[j]:
            return is_palindrome(a, i, j) or is_palindrome(b, i, j)
        i += 1
        j -= 1
    return True

## Structure
def check_palindrome_formation(a: str, b: str) -> bool:
    # Your code here

    pass