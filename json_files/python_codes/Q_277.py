##Question ID: 277

def knows(a: int, b:int) -> bool:
    pass

def findCelebrity(n: int) -> int:
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate

## Structure
def knows(a: int, b:int) -> bool:
    # Your code here

    pass