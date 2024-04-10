##Question ID: 1829

def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    totalUnits = 0
    for box in boxTypes:
        boxCount = min(truckSize, box[0])
        totalUnits += boxCount * box[1]
        truckSize -= boxCount
        if truckSize == 0:
            break
    
    return totalUnits

## Structure
def maximumUnits(boxTypes, truckSize):
    # Your code here

    pass