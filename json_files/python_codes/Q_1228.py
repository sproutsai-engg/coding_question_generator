##Question ID: 1228

def mctFromLeafValues(arr: List[int]) -> int:
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    maxs = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            maxs[i][j] = max(arr[i:j+1])

    for len_ in range(1, n):
        for i in range(n - len_):
            j = i + len_
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + maxs[i][k] * maxs[k+1][j])

    return dp[0][n - 1]

## Structure
def mctFromLeafValues(arr: List[int]) -> int:
    # Your code here

    pass