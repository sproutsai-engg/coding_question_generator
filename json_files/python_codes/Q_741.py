##Question ID: 741

def cherryPickup(self, grid: List[List[int]]) -> int:
    def dp(r1, c1, c2):
        r2 = r1 + c1 - c2
        if (r1 == len(grid) or r2 == len(grid) or c1 == len(grid) or c2 == len(grid) or
            grid[r1][c1] == -1 or grid[r2][c2] == -1):
            return float('-inf')
        elif r1 == len(grid) - 1 and c1 == len(grid) - 1:
            return grid[r1][c1]
        elif memo[r1][c1][c2] != float('-inf'):
            return memo[r1][c1][c2]
        else:
            memo[r1][c1][c2] = grid[r1][c1] + (r1 != r2) * grid[r2][c2]
            max_cherries = max(dp(r1 + 1, c1, c2 + 1), dp(r1, c1 + 1, c2 + 1),
                               dp(r1 + 1, c1, c2), dp(r1, c1 + 1, c2))
            memo[r1][c1][c2] += max_cherries
        
        return memo[r1][c1][c2]
    
    N = len(grid)
    memo = [[[float('-inf')] * N for _1 in range(N)] for _2 in range(N)]
    return max(0, dp(0, 0, 0))


## Structure
def cherryPickup(self, grid: List[List[int]]) -> int:
    # Your code here

    pass