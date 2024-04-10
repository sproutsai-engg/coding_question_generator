##Question ID: 1768

def mergeAlternately(word1: str, word2: str) -> str:
    result = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    result += word1[i:]
    result += word2[j:]
    return "".join(result)

## Structure
def mergeAlternately(word1: str, word2: str) -> str:
    # Your code here

    pass