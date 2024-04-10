##Question ID: 562

def longestLine(mat):
    rows, cols = len(mat), len(mat[0])
    max_length = 0
    dp = [[[0, 0, 0, 0] for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1:
                dp[r][c][0] = dp[r - 1][c][0] + 1 if r > 0 else 1
                dp[r][c][1] = dp[r][c - 1][1] + 1 if c > 0 else 1
                dp[r][c][2] = dp[r - 1][c - 1][2] + 1 if r > 0 and c > 0 else 1
                dp[r][c][3] = dp[r - 1][c + 1][3] + 1 if r > 0 and c < cols - 1 else 1
                max_length = max(max_length, max(dp[r][c]))

    return max_length


## Structure
def longestLine(mat):
    # Your code here

    pass