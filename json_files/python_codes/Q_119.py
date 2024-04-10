##Question ID: 119

def get_row(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(1, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]
    return row

## Structure
def get_row(rowIndex):
    # Your code here

    pass