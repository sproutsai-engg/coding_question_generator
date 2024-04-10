##Question ID: 1133

def last_substring(s: str) -> str:
    i, j, k, n = 0, 1, 0, len(s)
    while j + k < n:
        if s[i + k] == s[j + k]:
            k += 1
        elif s[i + k] < s[j + k]:
            i = j
            j += 1
            k = 0
        else:
            j += 1
            k = 0
    return s[i:]

## Structure
def last_substring(s: str) -> str:
    # Your code here

    pass