##Question ID: 1198

def smallest_common_element(mat):
    counts = {}
    for row in mat:
        for num in row:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] == len(mat):
                return num
    return -1

## Structure
def smallest_common_element(mat):
    # Your code here

    pass