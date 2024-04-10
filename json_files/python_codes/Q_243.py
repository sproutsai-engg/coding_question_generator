##Question ID: 243

def shortestDistance(wordsDict, word1, word2):
    idx1, idx2, minDistance = -1, -1, float('inf')
    for i, word in enumerate(wordsDict):
        if word == word1:
            idx1 = i
        if word == word2:
            idx2 = i
        if idx1 != -1 and idx2 != -1:
            minDistance = min(minDistance, abs(idx1 - idx2))
    return minDistance

## Structure
def shortestDistance(wordsDict, word1, word2):
    # Your code here

    pass