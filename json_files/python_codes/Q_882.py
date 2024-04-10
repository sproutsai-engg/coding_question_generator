##Question ID: 882

def peakIndexInMountainArray(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low

## Structure
def peakIndexInMountainArray(arr):
    # Your code here

    pass