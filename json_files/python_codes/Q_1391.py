##Question ID: 1391

def hasValidPath(grid):
    m, n = len(grid), len(grid[0])

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    allowed = [[], [0, 2], [1, 3], [0, 1], [0, 3], [1, 2], [1, 0]]

    visited = [[False] * n for _ in range(m)]

    def dfs(i, j):
        if i == m - 1 and j == n - 1:
            return True

        visited[i][j] = True
        for dir in allowed[grid[i][j]]:
            x, y = i + directions[dir][0], j + directions[dir][1]
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and (dir + 2) % 4 in allowed[grid[x][y]]:
                if dfs(x, y):
                    return True
        return False

    return dfs(0, 0)

## Structure
def hasValidPath(grid):
    # Your code here

    pass