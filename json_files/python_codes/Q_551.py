##Question ID: 551

def checkRecord(s: str) -> bool:
    late, absent = 0, 0
    for c in s:
        if c == 'A':
            absent += 1
            late = 0
        elif c == 'L':
            late += 1
        else:
            late = 0

        if absent >= 2 or late >= 3:
            return False
    return True

## Structure
def checkRecord(s: str) -> bool:
    # Your code here

    pass