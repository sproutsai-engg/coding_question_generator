##Question ID: 1311

def largestMagicSquare(grid):
    m, n = len(grid), len(grid[0])
    row = [[0] * (n + 1) for _ in range(m)]
    col = [[0] * n for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            row[i][j + 1] = row[i][j] + grid[i][j]
            col[i + 1][j] = col[i][j] + grid[i][j]

    for k in reversed(range(2, min(m, n) + 1)):
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                _sum = row[i][j + k] - row[i][j]
                ok = all(row[i + t][j + k] - row[i + t][j] == _sum for t in range(1, k)) and all(
                    col[i + k][j + t] - col[i][j + t] == _sum for t in range(1, k))

                if not ok: continue
                
                diag1 = sum(grid[i + t][j + t] for t in range(k))
                diag2 = sum(grid[i + t][j + k - 1 - t] for t in range(k))
                
                if diag1 == _sum and diag2 == _sum: return k

    return 1


## Structure
def largestMagicSquare(grid):
    # Your code here

    pass