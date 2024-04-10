##Question ID: 1914

def rotateGrid(grid, k):
    if not grid: return grid
    
    m, n = len(grid), len(grid[0])
    numLayers = min(m, n) // 2

    for layer in range(numLayers):
        numToRotate = (m - 2 * layer) * 2 + (n - 2 * layer - 2) * 2
        effective_k = k % numToRotate

        while effective_k:
            temp = grid[layer][layer]
            for i in range(layer + 1, m - layer): temp, grid[i][layer] = grid[i][layer], temp
            for j in range(layer + 1, n - layer): temp, grid[m - layer - 1][j] = grid[m - layer - 1][j], temp
            for i in range(m - layer - 2, layer - 1, -1): temp, grid[i][n - layer - 1] = grid[i][n - layer - 1], temp
            for j in range(n - layer - 2, layer, -1): temp, grid[layer][j] = grid[layer][j], temp
            effective_k -= 1

    return grid

## Structure
def rotateGrid(grid, k):
    # Your code here

    pass