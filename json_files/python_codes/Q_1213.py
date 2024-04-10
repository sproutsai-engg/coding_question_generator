##Question ID: 1213

def arraysIntersection(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    result = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            result.append(arr1[i])
            i, j, k = i + 1, j + 1, k + 1
        else:
            if arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
                i += 1
            elif arr2[j] <= arr3[k]:
                j += 1
            else:
                k += 1
    return result

## Structure
def arraysIntersection(arr1, arr2, arr3):
    # Your code here

    pass