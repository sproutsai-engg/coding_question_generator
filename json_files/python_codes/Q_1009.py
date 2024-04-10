##Question ID: 1009

def pancakeSort(arr):
    flips = []
    for size in range(len(arr), 1, -1):
        maxIdx = arr.index(max(arr[:size]))
        flips.extend([maxIdx + 1, size])
        arr[:maxIdx + 1] = reversed(arr[:maxIdx + 1])
        arr[:size] = reversed(arr[:size])
    return flips

## Structure
def pancakeSort(arr):
    # Your code here

    pass