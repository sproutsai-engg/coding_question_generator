##Question ID: 867

def new21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0 or n >= k + maxPts:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    s, ans = 1, 0

    for i in range(1, n + 1):
        dp[i] = s / maxPts
        if i < k:
            s += dp[i]
        else:
            ans += dp[i]
        if i >= maxPts:
            s -= dp[i - maxPts]

    return ans


## Structure
def new21Game(n: int, k: int, maxPts: int) -> float:
    # Your code here

    pass