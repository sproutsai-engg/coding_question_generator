##Question ID: 616

def addBoldTag(s: str, words: list) -> str:
    n = len(s)
    marked = [False] * n
    for word in words:
        pos = s.find(word)
        while pos != -1:
            for i in range(pos, pos + len(word)):
                marked[i] = True
            pos = s.find(word, pos + 1)
    result = []
    i = 0
    while i < n:
        if marked[i]:
            result.append("<b>")
            while i < n and marked[i]:
                result.append(s[i])
                i += 1
            result.append("</b>")
        else:
            result.append(s[i])
            i += 1
    return "".join(result)

## Structure
def addBoldTag(s: str, words: list) -> str:
    # Your code here

    pass