##Question ID: 1707

def can_transform(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
    return j == len(t)


## Structure
def can_transform(s, t):
    # Your code here

    pass