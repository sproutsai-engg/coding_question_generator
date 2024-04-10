##Question ID: 320

def generateAbbreviations(word):
    if not word:
        return [""]
    res = []
    for i in range(len(word) + 1):
        for item in generateAbbreviations(word[i+1:]):
            if i == 0 or not item or not item[0].isdigit():
                res.append(word[:i+1] + item)
            if item and item[0].isdigit():
                res.append(word[:i] + '1' + item)
    return res

## Structure
def generateAbbreviations(word):
    # Your code here

    pass