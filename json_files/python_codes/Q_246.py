##Question ID: 246

def isStrobogrammatic(num: str) -> bool:
    lookup = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1
    while left <= right:
        if num[left] not in lookup or lookup[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    return True

## Structure
def isStrobogrammatic(num: str) -> bool:
    # Your code here

    pass