##Question ID: 73

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    firstRow, firstCol = False, False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                if i == 0: firstRow = True
                if j == 0: firstCol = True
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if firstRow:
        for j in range(cols):
            matrix[0][j] = 0

    if firstCol:
        for i in range(rows):
            matrix[i][0] = 0

## Structure
def setZeroes(matrix):
    # Your code here

    pass