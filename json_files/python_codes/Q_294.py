##Question ID: 294

def canWin(currentState: str) -> bool:
    for i in range(len(currentState) - 1):
        if currentState[i] == '+' and currentState[i + 1] == '+':
            temp = currentState[:i] + "--" + currentState[i + 2:]
            if not canWin(temp):
                return True
    return False

## Structure
def canWin(currentState: str) -> bool:
    # Your code here

    pass