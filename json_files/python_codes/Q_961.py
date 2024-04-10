##Question ID: 961

def isLongPressedName(name: str, typed: str) -> bool:
    i, j = 0, 0
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif j == 0 or typed[j] != typed[j - 1]:
            return False
        j += 1
    return i == len(name)

## Structure
def isLongPressedName(name: str, typed: str) -> bool:
    # Your code here

    pass