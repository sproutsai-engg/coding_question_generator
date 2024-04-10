##Question ID: 120

def minimumTotal(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]

## Structure
def minimumTotal(triangle):
    # Your code here

    pass