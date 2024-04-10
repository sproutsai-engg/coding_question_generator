##Question ID: 939

def find_valid_permutations(s: str) -> int:
    n = len(s)
    MOD = 1000000007
    dp = [0] * (n + 2)
    dp[0] = 1

    for c in s:
        new_dp = [0] * (n + 2)
        if c == 'I':
            for i in range(n):
                new_dp[i + 1] = (new_dp[i + 1] + dp[i]) % MOD
        else:
            for i in range(n - 1, -1, -1):
                new_dp[i] = (new_dp[i + 1] + dp[i + 1]) % MOD
        dp = new_dp

    return dp[0]

## Structure
def find_valid_permutations(s: str) -> int:
    # Your code here

    pass