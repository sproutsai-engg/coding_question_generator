##Question ID: 981

def min_deletion_size(strs):
    num_deleted = 0
    for col in range(len(strs[0])):
        for row in range(1, len(strs)):
            if strs[row][col] < strs[row - 1][col]:
                num_deleted += 1
                break
    return num_deleted


## Structure
def min_deletion_size(strs):
    # Your code here

    pass