##Question ID: 311

def multiply(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:
                for l in range(n):
                    result[i][l] += mat1[i][j] * mat2[j][l]
    return result

## Structure
def multiply(mat1, mat2):
    # Your code here

    pass