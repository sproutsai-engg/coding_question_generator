##Question ID: 688

def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    memo = [[[-1.0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
    return self.helper(n, k, row, column, memo)

def helper(self, n, k, row, column, memo):
    if row < 0 or row >= n or column < 0 or column >= n:
        return 0.0
    if k == 0:
        return 1.0
    if memo[row][column][k] >= 0:
        return memo[row][column][k]

    result = 0.0
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for move in moves:
        result += self.helper(n, k - 1, row + move[0], column + move[1], memo) / 8

    memo[row][column][k] = result
    return result

## Structure
def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    # Your code here

    pass