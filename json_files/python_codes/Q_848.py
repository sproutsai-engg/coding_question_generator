##Question ID: 848

def shiftingLetters(s: str, shifts) -> str:
    for i in range(len(shifts) - 2, -1, -1):
        shifts[i] += shifts[i + 1] % 26

    result = list(s)
    for i in range(len(s)):
        result[i] = chr((ord(result[i]) - ord('a') + shifts[i] % 26) % 26 + ord('a'))
        
    return "".join(result)

## Structure
def shiftingLetters(s: str, shifts) -> str:
    # Your code here

    pass