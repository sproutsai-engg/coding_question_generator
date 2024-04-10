##Question ID: 1885

def count_homogenous(s: str) -> int:
    res, count, mod = 0, 1, 10**9 + 7
    for i in range(1, len(s)):
        count = count + 1 if s[i] == s[i - 1] else 1
        res = (res + count) % mod
    return res

## Structure
def count_homogenous(s: str) -> int:
    # Your code here

    pass