##Question ID: 1314

def matrix_block_sum(mat, k):
    m, n = len(mat), len(mat[0])
    answer = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for r in range(max(0, i - k), min(m, i + k + 1)):
                for c in range(max(0, j - k), min(n, j + k + 1)):
                    answer[i][j] += mat[r][c]
                    
    return answer

## Structure
def matrix_block_sum(mat, k):
    # Your code here

    pass