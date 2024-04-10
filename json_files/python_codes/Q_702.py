##Question ID: 702

def search(reader, target):
    left, right = 0, 1
    while reader.get(right) < target:
        left = right
        right <<= 1

    while left <= right:
        mid = left + ((right - left) >> 1)
        val = reader.get(mid)
        if val == target:
            return mid
        if val > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

## Structure
def search(reader, target):
    # Your code here

    pass