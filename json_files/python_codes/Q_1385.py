##Question ID: 1385

def findTheDistanceValue(arr1, arr2, d):
    distance = 0
    for a in arr1:
        found = True
        for b in arr2:
            if abs(a - b) <= d:
                found = False
                break
        if found:
            distance += 1
    return distance

## Structure
def findTheDistanceValue(arr1, arr2, d):
    # Your code here

    pass