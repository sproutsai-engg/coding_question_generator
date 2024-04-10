##Question ID: 59

def generateMatrix(n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    value, top, bottom, left, right = 1, 0, n - 1, 0, n - 1

    while value <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = value
            value += 1

        for i in range(top + 1, bottom + 1):
            matrix[i][right] = value
            value += 1

        if top < bottom and left < right:
            for i in range(right - 1, left - 1, -1):
                matrix[bottom][i] = value
                value += 1

            for i in range(bottom - 1, top, -1):
                matrix[i][left] = value
                value += 1

        top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1

    return matrix

## Structure
def generateMatrix(n: int) -> List[List[int]]:
    # Your code here

    pass