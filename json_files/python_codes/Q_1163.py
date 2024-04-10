##Question ID: 1163

def lastSubstring(s: str) -> str:
    maxIndex = 0
    curIndex = 1
    while curIndex < len(s):
        i = 0
        while curIndex + i < len(s) and s[maxIndex + i] == s[curIndex + i]:
            i += 1
        if curIndex + i == len(s):
            break
        if s[maxIndex + i] < s[curIndex + i]:
            maxIndex = curIndex
        curIndex += 1
    return s[maxIndex:]

## Structure
def lastSubstring(s: str) -> str:
    # Your code here

    pass