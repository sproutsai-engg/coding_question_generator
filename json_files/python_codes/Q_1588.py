##Question ID: 1588

def sumOddLengthSubarrays(arr):
    sum = 0
    n = len(arr)
    for i in range(n):
        oddSubarrays = ((i + 1) * (n - i) + 1) // 2
        sum += arr[i] * oddSubarrays
    return sum

## Structure
def sumOddLengthSubarrays(arr):
    # Your code here

    pass