##Question ID: 1679

def findLengthOfShortestSubarray(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    if left == n - 1:
        return 0

    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    result = min(right, n - left - 1)

    i, j = 0, right

    while i <= left and j < n:
        if arr[i] <= arr[j]:
            result = min(result, j - i - 1)
            i += 1
        else:
            j += 1

    return result


## Structure
def findLengthOfShortestSubarray(arr):
    # Your code here

    pass