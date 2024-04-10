##Question ID: 727

def min_window_sub_sequence(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for j in range(0, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]

    start, length = 0, m + 1
    for j in range(1, m + 1):
        if dp[n][j] != 0 and j - dp[n][j] < length:
            start = dp[n][j]
            length = j - start

    return "" if length == m + 1 else s1[start:start + length]

## Structure
def min_window_sub_sequence(s1: str, s2: str) -> str:
    # Your code here

    pass