##Question ID: 1540

def canConvertString(s: str, t: str, k: int) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        diff = (ord(t[i]) - ord(s[i]) + 26) % 26
        if diff > 0:
            count[diff] += 1
    for i in range(1, 26):
        if count[i] > 0:
            if count[i] * 26 - 26 + i > k:
                return False
    return True

## Structure
def canConvertString(s: str, t: str, k: int) -> bool:
    # Your code here

    pass