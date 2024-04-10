##Question ID: 878

def shiftingLetters(s: str, shifts: list[int]) -> str:
    n = len(s)
    for i in range(n - 2, -1, -1):
        shifts[i] = (shifts[i] + shifts[i + 1]) % 26
    
    result = []
    for i in range(n):
        result.append(chr(((ord(s[i]) - ord('a')) + shifts[i]) % 26 + ord('a')))
    
    return "".join(result)

## Structure
def shiftingLetters(s: str, shifts: list[int]) -> str:
    # Your code here

    pass