##Question ID: 118

def generate(numRows):
    pascalsTriangle = []
    for i in range(numRows):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(pascalsTriangle[i-1][j-1] + pascalsTriangle[i-1][j])
            row.append(1)
        pascalsTriangle.append(row)
    return pascalsTriangle

## Structure
def generate(numRows):
    # Your code here

    pass