##Question ID: 1628

def numSubmat(mat):
    m, n = len(mat), len(mat[0])
    dp = [[0] * n for _ in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                dp[i][j] = (1 if j == 0 else dp[i][j - 1] + 1)
                minWidth = dp[i][j]
                for k in range(i, -1, -1):
                    minWidth = min(minWidth, dp[k][j])
                    count += minWidth

    return count

## Structure
def numSubmat(mat):
    # Your code here

    pass