##Question ID: 1328

def breakPalindrome(palindrome: str) -> str:
    length = len(palindrome)
    if length == 1:
        return ""
    
    chars = list(palindrome)
    for i in range(length // 2):
        if chars[i] != 'a':
            chars[i] = 'a'
            return "".join(chars)
    
    chars[length - 1] = 'b'
    return "".join(chars)

## Structure
def breakPalindrome(palindrome: str) -> str:
    # Your code here

    pass