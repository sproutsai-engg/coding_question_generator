##Question ID: 857

def largeGroupPositions(s: str):
    result = []
    start = 0
    for i in range(1, len(s)):
        if s[i] != s[start]:
            if i - start >= 3:
                result.append([start, i - 1])
            start = i
    if len(s) - start >= 3:
        result.append([start, len(s) - 1])
    return result


## Structure
def largeGroupPositions(s: str):
    # Your code here

    pass