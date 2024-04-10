##Question ID: 1000

def min_deletion_size(strs):
    rows, cols = len(strs), len(strs[0])
    count = 0
    for c in range(cols):
        for r in range(1, rows):
            if strs[r - 1][c] > strs[r][c]:
                count += 1
                break
    return count


## Structure
def min_deletion_size(strs):
    # Your code here

    pass