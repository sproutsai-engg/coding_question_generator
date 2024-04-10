##Question ID: 999

def regionsBySlashes(grid):
    n = len(grid)
    graph = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '/':
                graph[i * 3][j * 3 + 2] = graph[i * 3 + 1][j * 3 + 1] = graph[i * 3 + 2][j * 3] = 1
            if grid[i][j] == '\\':
                graph[i * 3][j * 3] = graph[i * 3 + 1][j * 3 + 1] = graph[i * 3 + 2][j * 3 + 2] = 1

    regions = 0
    for i in range(n * 3):
        for j in range(n * 3):
            if not graph[i][j]:
                regions += 1
                dfs(graph, i, j)

    return regions

def dfs(graph, i, j):
    n = len(graph)
    if i < 0 or j < 0 or i >= n or j >= n or graph[i][j]:
        return

    graph[i][j] = 1
    dfs(graph, i - 1, j)
    dfs(graph, i + 1, j)
    dfs(graph, i, j - 1)
    dfs(graph, i, j + 1)

## Structure
def regionsBySlashes(grid):
    # Your code here

    pass