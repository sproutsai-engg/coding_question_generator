##Question ID: 1094

def allCellsDistOrder(rows, cols, rCenter, cCenter):
    coordinates = [[i, j] for i in range(rows) for j in range(cols)]

    coordinates.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

    return coordinates

## Structure
def allCellsDistOrder(rows, cols, rCenter, cCenter):
    # Your code here

    pass