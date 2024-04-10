##Question ID: 769

def orderOfLargestPlusSign(n, mines):
    grid = [[1] * n for _ in range(n)]
    for mine in mines:
        grid[mine[0]][mine[1]] = 0
        
    left, right, up, down = [list(grid) for _ in range(4)]

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                left[i][j] = 1 + (left[i][j - 1] if j > 0 else 0)
                up[i][j] = 1 + (up[i - 1][j] if i > 0 else 0)

    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if grid[i][j]:
                right[i][j] = 1 + (right[i][j + 1] if j < n - 1 else 0)
                down[i][j] = 1 + (down[i + 1][j] if i < n - 1 else 0)
                ans = max(ans, min([left[i][j], right[i][j], up[i][j], down[i][j]]))

    return ans


## Structure
def orderOfLargestPlusSign(n, mines):
    # Your code here

    pass