##Question ID: 125

def isPalindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

## Structure
def isPalindrome(s: str) -> bool:
    # Your code here

    pass