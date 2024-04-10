##Question ID: 845

def longestMountain(arr):
    n = len(arr)
    res = up = down = 0

    for i in range(1, n):
        if (down and arr[i - 1] < arr[i]) or arr[i - 1] == arr[i]:
            up = down = 0

        up += arr[i - 1] < arr[i]
        down += arr[i - 1] > arr[i]

        if up and down:
            res = max(res, up + down + 1)

    return res

## Structure
def longestMountain(arr):
    # Your code here

    pass