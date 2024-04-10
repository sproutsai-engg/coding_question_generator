##Question ID: 1217

def sort_array(arr1, arr2):
    counts = {}
    result = []

    for num in arr1:
        counts[num] = counts.get(num, 0) + 1

    for num in arr2:
        if num in counts:
            result.extend([num] * counts[num])
            del counts[num]

    for num in sorted(counts.keys()):
        result.extend([num] * counts[num])

    return result

## Structure
def sort_array(arr1, arr2):
    # Your code here

    pass