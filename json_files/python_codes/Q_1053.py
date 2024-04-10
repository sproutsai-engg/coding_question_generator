##Question ID: 1053

def prevPermOpt1(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            j = i + 1
            while j < n and arr[j] < arr[i]:
                j += 1
            arr[i], arr[j - 1] = arr[j - 1], arr[i]
            break
    return arr


## Structure
def prevPermOpt1(arr):
    # Your code here

    pass