##Question ID: 1331

def getMaximumGold(grid):
    m, n, max_gold = len(grid), len(grid[0]), 0

    def getMaximumGoldHelper(x, y):
        if not (0 <= x < m) or not (0 <= y < n) or grid[x][y] == 0:
            return 0

        original_gold = grid[x][y]
        grid[x][y] = 0

        max_gold = 0
        max_gold = max(max_gold, getMaximumGoldHelper(x + 1, y))
        max_gold = max(max_gold, getMaximumGoldHelper(x - 1, y))
        max_gold = max(max_gold, getMaximumGoldHelper(x, y + 1))
        max_gold = max(max_gold, getMaximumGoldHelper(x, y - 1))

        grid[x][y] = original_gold
        return max_gold + original_gold

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                max_gold = max(max_gold, getMaximumGoldHelper(i, j))

    return max_gold


## Structure
def getMaximumGold(grid):
    # Your code here

    pass