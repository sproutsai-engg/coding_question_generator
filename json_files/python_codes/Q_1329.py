##Question ID: 1329

def minCostToMoveChips(position):
    evenCount, oddCount = 0, 0
    for i in position:
        if i % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    return min(evenCount, oddCount)

## Structure
def minCostToMoveChips(position):
    # Your code here

    pass