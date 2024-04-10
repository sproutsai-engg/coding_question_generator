##Question ID: 841

def shortestToChar(s, c):
    n = len(s)
    result = [n for _ in range(n)]
    pos = -n

    for i in range(n):
        if s[i] == c:
            pos = i
        result[i] = i - pos

    for i in range(pos - 1, -1, -1):
        if s[i] == c:
            pos = i
        result[i] = min(result[i], pos - i)

    return result


## Structure
def shortestToChar(s, c):
    # Your code here

    pass