##Question ID: 916

def find_kth_character(s: str, k: int) -> str:
    n = len(s)
    size = 0

    for c in s:
        if c.isdigit():
            size = size * int(c)
        else:
            size += 1

    for i in range(n - 1, -1, -1):
        c = s[i]
        k %= size
        if k == 0 and not c.isdigit():
            return c

        if c.isdigit():
            size //= int(c)
        else:
            size -= 1

    return '-'

## Structure
def find_kth_character(s: str, k: int) -> str:
    # Your code here

    pass