##Question ID: 777

def isToeplitzMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True


## Structure
def isToeplitzMatrix(matrix):
    # Your code here

    pass