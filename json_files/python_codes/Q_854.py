##Question ID: 854

def kSimilarity(s1: str, s2: str) -> int:
    k = 0
    temp = list(s1)

    for i in range(len(temp)):
        if temp[i] != s2[i]:
            j = i + 1
            while temp[j] != s2[i] or s2[j] == temp[j]:
                j += 1
            temp[i], temp[j] = temp[j], temp[i]
            k += 1

    return k

## Structure
def kSimilarity(s1: str, s2: str) -> int:
    # Your code here

    pass