##Question ID: 1541

def minInsertions(s: str) -> int:
    left = 0
    res = 0
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '(':
            left += 1
        else:
            if left == 0: 
                res += 1
            else: 
                left -= 1
            if i == n - 1 or s[i + 1] != ')':
                res += 1
                i += 1
        i += 1
    return res + left * 2

## Structure
def minInsertions(s: str) -> int:
    # Your code here

    pass