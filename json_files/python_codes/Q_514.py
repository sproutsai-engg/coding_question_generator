##Question ID: 514

def find_rotate_steps(ring: str, key: str) -> int:
    n, m = len(ring), len(key)
    dp = [[0] * n for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n):
            dp[i][j] = float('inf')
            for k in range(n):
                if ring[k] == key[i]:
                    diff = abs(j - k)
                    step = min(diff, n - diff)
                    dp[i][j] = min(dp[i][j], step + dp[i + 1][k])

    return dp[0][0] + m


## Structure
def find_rotate_steps(ring: str, key: str) -> int:
    # Your code here

    pass