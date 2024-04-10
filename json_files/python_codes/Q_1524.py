##Question ID: 1524

def stringMatching(words):
    result = []
    for word1 in words:
        for word2 in words:
            if word1 != word2 and word1 in word2:
                result.append(word1)
                break
    return result

## Structure
def stringMatching(words):
    # Your code here

    pass