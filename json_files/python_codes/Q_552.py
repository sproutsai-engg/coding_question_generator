##Question ID: 552

def checkRecord(n: int) -> int:
    M = 1000000007
    dp = [1] * 6  # [latent state 0, latent state 1, ..., latent state 5]
    while n:
        next_dp = [0] * 6
        next_dp[0] = (dp[0] + dp[1] + dp[2]) % M
        next_dp[1] = dp[0]
        next_dp[2] = dp[1]
        next_dp[3] = (dp[3] + dp[4] + dp[5]) % M
        next_dp[4] = dp[3]
        next_dp[5] = dp[4]
        dp = next_dp
        n -= 1
    return sum(dp) % M


## Structure
def checkRecord(n: int) -> int:
    # Your code here

    pass