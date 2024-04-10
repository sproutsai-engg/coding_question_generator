##Question ID: 963

def find_same_binary_value_parts(arr):
    ones = sum(arr)

    if ones % 3 != 0:
        return [-1, -1]

    target = ones // 3
    if target == 0:
        return [0, len(arr) - 2]

    count = 0
    i = j = -1
    ones = 0
    for idx, n in enumerate(arr):
        if n == 1:
            ones += 1
            if ones == target + 1:
                count += 1
            if count == 1 and i == -1:
                i = idx
            if count == 2 and j == -1:
                j = idx
            if count == 3:
                break

    return [i, j]

## Structure
def find_same_binary_value_parts(arr):
    # Your code here

    pass