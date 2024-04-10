##Question ID: 1894

def merge_alternately(word1, word2):
    merged = []
    i, j = 0, 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            merged.append(word1[i])
            i += 1
        if j < len(word2):
            merged.append(word2[j])
            j += 1
    return "".join(merged)

## Structure
def merge_alternately(word1, word2):
    # Your code here

    pass