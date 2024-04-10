##Question ID: 1625

def findLexSmallestString(s: str, a: int, b: int) -> str:
    def add_odd(s: str, a: int) -> str:
        return ''.join([str((int(ch) + a) % 10) if idx % 2 else ch for idx, ch in enumerate(s)])

    def rotate(s: str, k: int) -> str:
        k %= len(s)
        return s[-k:] + s[:-k]

    smallest = s
    for _ in range(len(s)):
        for _ in range(10):
            rotated = rotate(s, b)
            temp = add_odd(rotated, a)
            smallest = min(smallest, temp)
            s = rotated
        s = add_odd(s, a)
    return smallest

## Structure
def findLexSmallestString(s: str, a: int, b: int) -> str:
    # Your code here

    pass