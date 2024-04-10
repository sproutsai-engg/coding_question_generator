##Question ID: 1221

def find_special_integer(arr):
    n = len(arr)
    required_count = n // 4
    for i in range(n):
        if arr[i] == arr[i + required_count]:
            return arr[i]
    return -1

## Structure
def find_special_integer(arr):
    # Your code here

    pass