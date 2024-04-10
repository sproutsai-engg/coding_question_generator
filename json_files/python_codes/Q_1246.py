##Question ID: 1246

def minimumMoves(arr):
    def minRemovals(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]

        ans = minRemovals(i + 1, j) + 1
        for k in range(i + 1, j + 1):
            if arr[i] == arr[k]:
                ans = min(ans, minRemovals(i + 1, k - 1) + minRemovals(k + 1, j))
        dp[i][j] = ans
        return ans

    dp = [[-1] * len(arr) for _ in range(len(arr))]
    return minRemovals(0, len(arr) - 1)

## Structure
def minimumMoves(arr):
    # Your code here

    pass