##Question ID: 161

def isOneEditDistance(s: str, t: str) -> bool:
    m, n = len(s), len(t)
    if m > n:
        return isOneEditDistance(t, s)
    if n - m > 1:
        return False
    for i in range(m):
        if s[i] != t[i]:
            return s[i + (m < n):] == t[i + 1:]
    return m + 1 == n

## Structure
def isOneEditDistance(s: str, t: str) -> bool:
    # Your code here

    pass