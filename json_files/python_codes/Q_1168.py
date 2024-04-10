##Question ID: 1168

def duplicateZeros(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        if arr[i] == 0:
            for j in range(n - 2, i, -1):
                arr[j + 1] = arr[j]
            arr[i + 1] = 0
            i += 2
        else:
            i += 1

## Structure
def duplicateZeros(arr):
    # Your code here

    pass