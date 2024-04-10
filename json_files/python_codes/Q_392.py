##Question ID: 392

def is_subsequence(s, t):
    si, ti = 0, 0

    while si < len(s) and ti < len(t):
        if s[si] == t[ti]:
            si += 1
        ti += 1

    return si == len(s)


## Structure
def is_subsequence(s, t):
    # Your code here

    pass