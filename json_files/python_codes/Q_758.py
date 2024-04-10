##Question ID: 758

def addBoldTag(words, s):
    bold = [False] * len(s)
    for word in words:
        pos = s.find(word)
        while pos != -1:
            for i in range(pos, pos + len(word)):
                bold[i] = True
            pos = s.find(word, pos + 1)

    result = []
    for i in range(len(s)):
        if bold[i] and (i == 0 or not bold[i - 1]):
            result.append("<b>")
        result.append(s[i])
        if bold[i] and (i == len(s) - 1 or not bold[i + 1]):
            result.append("</b>")

    return "".join(result)

## Structure
def addBoldTag(words, s):
    # Your code here

    pass