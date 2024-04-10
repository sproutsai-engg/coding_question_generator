##Question ID: 1895

def min_operations(boxes: str):
    result = [0] * len(boxes)
    count, total = 0, 0

    for i in range(len(boxes)):
        total += count
        result[i] = total
        if boxes[i] == '1':
            count += 1

    count, total = 0, 0
    for i in range(len(boxes) - 1, -1, -1):
        total += count
        result[i] += total
        if boxes[i] == '1':
            count += 1

    return result

## Structure
def min_operations(boxes: str):
    # Your code here

    pass