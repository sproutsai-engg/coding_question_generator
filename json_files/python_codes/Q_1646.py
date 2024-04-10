##Question ID: 1646

def findKthPositive(arr, k):
    i, num = 0, 1
    while k > 0:
        if i < len(arr) and arr[i] == num:
            i += 1
        else:
            k -= 1
        num += 1
    return num - 1

## Structure
def findKthPositive(arr, k):
    # Your code here

    pass