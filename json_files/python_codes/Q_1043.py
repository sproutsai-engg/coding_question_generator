##Question ID: 1043

def grid_illumination(n, lamps, queries):
    lamp_rows = set()
    lamp_cols = set()
    lamp_left_diag = set()
    lamp_right_diag = set()

    for lamp in lamps:
        row, col = lamp
        lamp_rows.add(row)
        lamp_cols.add(col)
        lamp_left_diag.add(row - col)
        lamp_right_diag.add(row + col)

    ans = []

    for query in queries:
        row, col = query
        if row in lamp_rows or col in lamp_cols or (row - col) in lamp_left_diag or (row + col) in lamp_right_diag:
            ans.append(1)
        else:
            ans.append(0)
        for i in range(-1, 2):
            for j in range(-1, 2):
                newRow, newCol = row + i, col + j
                lamp_rows.discard(newRow)
                lamp_cols.discard(newCol)
                lamp_left_diag.discard(newRow - newCol)
                lamp_right_diag.discard(newRow + newCol)

    return ans


## Structure
def grid_illumination(n, lamps, queries):
    # Your code here

    pass