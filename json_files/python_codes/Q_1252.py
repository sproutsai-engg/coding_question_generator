##Question ID: 1252

def break_palindrome(palindrome: str) -> str:
    n = len(palindrome)
    if n < 2:
        return ""
    
    palindrome = list(palindrome)
    for i in range(n // 2):
        if palindrome[i] != 'a':
            palindrome[i] = 'a'
            return "".join(palindrome)
    
    palindrome[-1] = 'b'
    return "".join(palindrome)

## Structure
def break_palindrome(palindrome: str) -> str:
    # Your code here

    pass