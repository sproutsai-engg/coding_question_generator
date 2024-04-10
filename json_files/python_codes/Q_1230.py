##Question ID: 1230

def max_value(arr1, arr2):
    n = len(arr1)
    max1 = max2 = max3 = max4 = float('-inf')
    min1 = min2 = min3 = min4 = float('inf')

    for i in range(n):
        max1 = max(max1, arr1[i] - arr2[i] + i)
        max2 = max(max2, arr1[i] + arr2[i] + i)
        max3 = max(max3, -arr1[i] + arr2[i] + i)
        max4 = max(max4, -arr1[i] - arr2[i] + i)

        min1 = min(min1, arr1[i] - arr2[i] + i)
        min2 = min(min2, arr1[i] + arr2[i] + i)
        min3 = min(min3, -arr1[i] + arr2[i] + i)
        min4 = min(min4, -arr1[i] - arr2[i] + i)

    return max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)


## Structure
def max_value(arr1, arr2):
    # Your code here

    pass