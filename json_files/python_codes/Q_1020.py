##Question ID: 1020

def maxTurbulenceSize(arr):
    n = len(arr)
    result = 1
    i = 0

    while i < n - 1:
        if arr[i] == arr[i + 1]:
            i += 1
            continue

        j = i + 1
        while j < n - 1 and ((arr[j] > arr[j + 1]) != (arr[j - 1] > arr[j])):
            j += 1
        
        result = max(result, j - i + 1)
        i = j

    return result


## Structure
def maxTurbulenceSize(arr):
    # Your code here

    pass