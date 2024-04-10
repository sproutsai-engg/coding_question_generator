##Question ID: 370

def get_updated_array(length, updates):
    arr = [0] * length

    for start, end, inc in updates:
        arr[start] += inc
        if end + 1 < length:
            arr[end + 1] -= inc

    for i in range(1, length):
        arr[i] += arr[i - 1]

    return arr

## Structure
def get_updated_array(length, updates):
    # Your code here

    pass