##Question ID: 54

def spiralOrder(matrix):
    result = []
    if not matrix: return result
    m, n = len(matrix), len(matrix[0])
    rowStart, colStart, rowEnd, colEnd = 0, 0, m - 1, n - 1

    while rowStart <= rowEnd and colStart <= colEnd:
        for i in range(colStart, colEnd + 1): 
            result.append(matrix[rowStart][i])
        rowStart += 1
        
        for i in range(rowStart, rowEnd + 1): 
            result.append(matrix[i][colEnd]) 
        colEnd -= 1
        
        if rowStart <= rowEnd:
            for i in range(colEnd, colStart - 1, -1): 
                result.append(matrix[rowEnd][i]) 
        rowEnd -= 1
        
        if colStart <= colEnd:
            for i in range(rowEnd, rowStart - 1, -1): 
                result.append(matrix[i][colStart]) 
        colStart += 1
        
    return result

## Structure
def spiralOrder(matrix):
    # Your code here

    pass