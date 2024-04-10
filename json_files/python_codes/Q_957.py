##Question ID: 957

def minAddToMakeValid(s: str) -> int:
    result = balance = 0
    for c in s:
        balance += 1 if c == '(' else -1
        if balance == -1:
            result += 1
            balance += 1
    return result + balance

## Structure
def minAddToMakeValid(s: str) -> int:
    # Your code here

    pass