##Question ID: 600

def findIntegers(n: int) -> int:
    dp = [[0, 0] for _ in range(32)]
    dp[0][0], dp[0][1] = 1, 1

    for i in range(1, 32):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]

    ans = 0
    prev_bit = 0
    for i in range(30, -1, -1):
        if n & (1 << i):
            ans += dp[i][0]
            if prev_bit:
                break
            prev_bit = 1
        else:
            prev_bit = 0

    return ans + 1


## Structure
def findIntegers(n: int) -> int:
    # Your code here

    pass