##Question ID: 466

def getMaxRepetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    count1, count2, i, j = 0, 0, 0, 0
    while count1 < n1:
        if s1[i] == s2[j]:
            j += 1
            if j == len(s2):
                j = 0
                count2 += 1
        i += 1
        if i == len(s1):
            i = 0
            count1 += 1
    return count2 // n2


## Structure
def getMaxRepetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    # Your code here

    pass