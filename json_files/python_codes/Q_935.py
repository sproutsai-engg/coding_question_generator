##Question ID: 935

def lex_smallest_string(s, k):
    res = s
    for i in range(k):
        tmp = s[i:] + s[:i]
        if tmp < res:
            res = tmp
    return res

## Structure
def lex_smallest_string(s, k):
    # Your code here

    pass