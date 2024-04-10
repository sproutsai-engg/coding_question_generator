##Question ID: 1846

def maximumElementAfterDecrementingAndRearranging(arr: List[int]) -> int:
    arr.sort()
    arr[0] = 1
    for i in range(1, len(arr)):
        arr[i] = min(arr[i], arr[i - 1] + 1)
    return arr[-1]

## Structure
def maximumElementAfterDecrementingAndRearranging(arr: List[int]) -> int:
    # Your code here

    pass