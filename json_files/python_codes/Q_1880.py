##Question ID: 1880

def largest_merge(word1: str, word2: str) -> str:
    merge = []
    while word1 or word2:
        if word1 > word2:
            merge.append(word1[0])
            word1 = word1[1:]
        else:
            merge.append(word2[0])
            word2 = word2[1:]
    return ''.join(merge)

## Structure
def largest_merge(word1: str, word2: str) -> str:
    # Your code here

    pass