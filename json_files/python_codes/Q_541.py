##Question ID: 541

def reverseStr(s, k):
    chars = list(s)
    for i in range(0, len(chars), 2 * k):
        chars[i:i + k] = reversed(chars[i:i + k])
    return "".join(chars)

## Structure
def reverseStr(s, k):
    # Your code here

    pass