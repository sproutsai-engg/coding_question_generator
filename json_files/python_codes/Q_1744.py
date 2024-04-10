##Question ID: 1744

def num_ways(words, target):
    n, m = len(words), len(target)
    MOD = 10**9 + 7
    cnt = [0] * 26
    for word in words:
        for ch in word:
            cnt[ord(ch) - ord('a')] += 1
    dp = [0] * (m + 1)
    dp[0] = 1
    for ch in target:
        for i in range(m - 1, -1, -1):
            dp[i + 1] += dp[i] * cnt[ord(ch) - ord('a')]
            dp[i + 1] %= MOD
    return dp[m]

## Structure
def num_ways(words, target):
    # Your code here

    pass