##Question ID: 1564

def maxBoxesInWarehouse(boxes, warehouse):
    n = len(warehouse)
    for i in range(1, n):
        warehouse[i] = min(warehouse[i], warehouse[i - 1])
    boxes.sort(reverse=True)
    boxIndex = 0
    boxesCount = 0
    for i in range(n):
        if boxIndex < len(boxes) and boxes[boxIndex] <= warehouse[i]:
            boxesCount += 1
            boxIndex += 1
    return boxesCount


## Structure
def maxBoxesInWarehouse(boxes, warehouse):
    # Your code here

    pass