##Question ID: 361

def maxKilledEnemies(grid):
    if not grid: return 0
    m, n, result, rowhits = len(grid), len(grid[0]), 0, 0
    colhits = [0] * n
    for i in range(m):
        for j in range(n):
            if j == 0 or grid[i][j - 1] == 'W':
                rowhits = 0
                k = j
                while k < n and grid[i][k] != 'W':
                    rowhits += grid[i][k] == 'E'
                    k += 1
            if i == 0 or grid[i - 1][j] == 'W':
                colhits[j] = 0
                k = i
                while k < m and grid[k][j] != 'W':
                    colhits[j] += grid[k][j] == 'E'
                    k += 1
            if grid[i][j] == '0':
                result = max(result, rowhits + colhits[j])
    return result

## Structure
def maxKilledEnemies(grid):
    # Your code here

    pass