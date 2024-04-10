##Question ID: 1486

def findTheDistanceValue(arr1, arr2, d):
    count = 0
    for i in arr1:
        valid = True
        for j in arr2:
            if abs(i - j) <= d:
                valid = False
                break
        if valid:
            count += 1
    return count

## Structure
def findTheDistanceValue(arr1, arr2, d):
    # Your code here

    pass