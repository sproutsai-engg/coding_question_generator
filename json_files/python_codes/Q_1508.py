##Question ID: 1508

def longestHappyPrefix(s):
    n = len(s)
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return s[:lps[-1]]

## Structure
def longestHappyPrefix(s):
    # Your code here

    pass