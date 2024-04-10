##Question ID: 972

def knightDialer(n: int) -> int:
    if n == 1:
        return 10
    MOD = 10**9 + 7
    moves = [
        [4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
        [], [1, 7, 0], [2, 6], [1, 3], [2, 4]
    ]
    dp = [1] * 10
    for _ in range(2, n + 1):
        new_dp = [0] * 10
        for j in range(10):
            for move in moves[j]:
                new_dp[j] = (new_dp[j] + dp[move]) % MOD
        dp = new_dp
    return sum(dp) % MOD

## Structure
def knightDialer(n: int) -> int:
    # Your code here

    pass