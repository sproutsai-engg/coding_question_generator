##Question ID: 1883

def minSkips(dist, speed, hoursBefore):
    n = len(dist)
    dp = [[1e9] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(i+1):
            t = dist[i] / speed + (1 if j else 0)
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + t)
            skipped_t = -(-dist[i] / speed) - dp[i][j]
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + skipped_t)

    for i in range(n + 1):
        if dp[n][i] <= hoursBefore:
            return i
    return -1

## Structure
def minSkips(dist, speed, hoursBefore):
    # Your code here

    pass