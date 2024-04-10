##Question ID: 1637

def min_length_encoded(s: str, k: int) -> int:
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(k + 1):
            cnt = 1
            dp[i][j] = i - j
            l = i - 2
            while l >= 0 and i - 2 - l <= j:
                if s[l] == s[i - 1]:
                    cnt += 1
                else:
                    cnt = 1
                used = i - 2 - l
                new_aposition = i - 1 - cnt - used + 1
                if cnt >= 100:
                    new_aposition += 4
                elif cnt >= 10:
                    new_aposition += 3
                elif cnt >= 2:
                    new_aposition += 2
                else:
                    new_aposition += 1
                dp[i][j] = min(dp[i][j], new_aposition + dp[l][j - used])
                l -= 1

    return dp[n][k]

## Structure
def min_length_encoded(s: str, k: int) -> int:
    # Your code here

    pass