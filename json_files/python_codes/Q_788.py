##Question ID: 788

def rotatedDigits(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if isGood(i):
            count += 1
    return count

def isGood(num: int) -> bool:
    changed = False
    while num:
        digit = num % 10
        if digit in (3, 4, 7):
            return False
        if digit in (2, 5, 6, 9):
            changed = True
        num //= 10
    return changed

## Structure
def rotatedDigits(n: int) -> int:
    # Your code here

    pass