##Question ID: 1089

def duplicateZeros(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        if arr[i] == 0:
            for j in range(n - 1, i + 1, -1):
                arr[j] = arr[j - 1]
            arr[i + 1] = 0
            i += 1
        i += 1

## Structure
def duplicateZeros(arr):
    # Your code here

    pass