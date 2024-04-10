##Question ID: 639

def num_decodings(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 9 if s[0] == '*' else (0 if s[0] == '0' else 1)

    for i in range(2, n + 1):
        c, prev_c = s[i - 1], s[i - 2]
        
        if c == '*':
            dp[i] = 9 * dp[i - 1]
            if prev_c == '1': dp[i] += 9 * dp[i - 2]
            elif prev_c == '2': dp[i] += 6 * dp[i - 2]
            elif prev_c == '*': dp[i] += 15 * dp[i - 2]
        else:
            dp[i] = dp[i - 1] if c != '0' else 0
            num = int(s[i - 2 : i])
            if prev_c == '1' or (prev_c == '2' and num <= 26): dp[i] += dp[i - 2]
            elif prev_c == '*': dp[i] += 2 * dp[i - 2] if 10 <= num <= 26 else dp[i - 2]

        dp[i] %= MOD
    return dp[n]

## Structure
def num_decodings(s: str) -> int:
    # Your code here

    pass