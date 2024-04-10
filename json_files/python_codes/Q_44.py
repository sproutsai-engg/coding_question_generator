##Question ID: 44

def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    i = j = 0
    match = asterisk = -1
    while i < m:
        if j < n and (s[i] == p[j] or p[j] == '?'):
            i, j = i + 1, j + 1
        elif j < n and p[j] == '*':
            match, asterisk = i, j
            j += 1
        elif asterisk >= 0:
            i, j = match + 1, asterisk + 1
            match += 1
        else:
            return False
    while j < n and p[j] == '*':
        j += 1
    return j == n

## Structure
def is_match(s: str, p: str) -> bool:
    # Your code here

    pass