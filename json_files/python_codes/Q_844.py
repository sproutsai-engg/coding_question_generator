##Question ID: 844

def backspaceCompare(s: str, t: str) -> bool:
    i, j = len(s) - 1, len(t) - 1
    while True:
        back = 0
        while i >= 0 and (back > 0 or s[i] == '#'):
            back = back + 1 if s[i] == '#' else back - 1
            i -= 1
        back = 0
        while j >= 0 and (back > 0 or t[j] == '#'):
            back = back + 1 if t[j] == '#' else back - 1
            j -= 1
        if i >= 0 and j >= 0 and s[i] == t[j]:
            i, j = i -1, j - 1
        else:
            return i == -1 and j == -1

## Structure
def backspaceCompare(s: str, t: str) -> bool:
    # Your code here

    pass