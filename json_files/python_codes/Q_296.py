##Question ID: 296

def minTotalDistance(grid):
    m, n = len(grid), len(grid[0])
    rows, cols = [], []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                rows.append(i)
                cols.append(j)

    cols.sort()
    row_median, col_median = rows[len(rows) // 2], cols[len(cols) // 2]
    distance = sum(abs(i - row_median) for i in rows) + sum(abs(j - col_median) for j in cols)
    return distance

## Structure
def minTotalDistance(grid):
    # Your code here

    pass