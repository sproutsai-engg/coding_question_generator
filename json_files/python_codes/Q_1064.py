##Question ID: 1064

def fixedPoint(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        middle = left + (right - left) // 2
        if arr[middle] < middle:
            left = middle + 1
        else:
            right = middle
    return left if arr[left] == left else -1

## Structure
def fixedPoint(arr: List[int]) -> int:
    # Your code here

    pass