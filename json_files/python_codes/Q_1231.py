##Question ID: 1231

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr

## Structure
def replaceElements(arr):
    # Your code here

    pass