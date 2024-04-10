##Question ID: 1539

def find_diagonal_order(nums):
    diagonals = {}
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i + j not in diagonals:
                diagonals[i + j] = []
            diagonals[i + j].append(nums[i][j])

    res = []
    for key in diagonals:
        res.extend(reversed(diagonals[key]))

    return res

## Structure
def find_diagonal_order(nums):
    # Your code here

    pass