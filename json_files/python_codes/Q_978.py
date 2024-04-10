##Question ID: 978

def valid_mountain_array(arr):
    n, i, j = len(arr), 0, len(arr) - 1
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    while j > 0 and arr[j - 1] > arr[j]:
        j -= 1
    return i > 0 and i == j and j < n - 1

## Structure
def valid_mountain_array(arr):
    # Your code here

    pass