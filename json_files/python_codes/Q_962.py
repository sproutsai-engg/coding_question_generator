##Question ID: 962

def minFlipsMonoIncr(s: str) -> int:
    flipCount, oneCount = 0, 0
    for c in s:
        if c == '1':
            oneCount += 1
        else:
            flipCount = min(flipCount + 1, oneCount)
    return flipCount

## Structure
def minFlipsMonoIncr(s: str) -> int:
    # Your code here

    pass