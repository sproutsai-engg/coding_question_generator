##Question ID: 74

def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m * n - 1

    while l <= r:
        mid = l + (r - l) // 2
        mid_val = matrix[mid // n][mid % n]

        if mid_val == target:
            return True
        elif mid_val < target:
            l = mid + 1
        else:
            r = mid - 1

    return False

## Structure
def searchMatrix(matrix, target):
    # Your code here

    pass