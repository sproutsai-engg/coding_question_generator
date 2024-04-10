##Question ID: 484

def findPermutation(s: str) -> list[int]:
    perm = [0] * (len(s) + 1)
    left = 1
    i = 0
    while i < len(s):
        if s[i] == 'I':
            perm[i] = left
            left += 1
            while i + 1 < len(s) and s[i + 1] == 'D':
                i += 1
        i += 1
    perm[len(s)] = left
    left += 1
    for i in reversed(range(len(s))):
        if s[i] == 'D':
            perm[i] = left
            left += 1
    return perm

## Structure
def findPermutation(s: str) -> list[int]:
    # Your code here

    pass