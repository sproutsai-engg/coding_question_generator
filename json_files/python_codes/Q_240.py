##Question ID: 240

def searchMatrix(matrix, target):
    row, col = len(matrix) - 1, 0
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:
            return True
    return False

## Structure
def searchMatrix(matrix, target):
    # Your code here

    pass