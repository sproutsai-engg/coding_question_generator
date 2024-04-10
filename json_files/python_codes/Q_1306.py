##Question ID: 1306

def minimumAbsDifference(arr):
    arr.sort()
    min_difference = float('inf')
    result = []

    for i in range(1, len(arr)):
        difference = arr[i] - arr[i - 1]
        if difference < min_difference:
            min_difference = difference
            result = [[arr[i - 1], arr[i]]]
        elif difference == min_difference:
            result.append([arr[i - 1], arr[i]])

    return result

## Structure
def minimumAbsDifference(arr):
    # Your code here

    pass