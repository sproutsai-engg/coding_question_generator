##Question ID: 1913

def min_changes(nums, k):
    n = len(nums)
    xor_prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        xor_prefix[i] = xor_prefix[i - 1] ^ nums[i - 1]

    dp = [{} for _ in range(k)]
    min_dp = [n] * k

    for i in range(1, n + 1):
        x = xor_prefix[i] ^ xor_prefix[i - k]

        if i >= k:
            dp[0][x] = dp[0].get(x, 0) + 1

        for j in range(1, 1 + (i - j * k) // k):
            if x in dp[j - 1]:
                dp[j][x] = dp[j].get(x, 0) + 1
                min_dp[j] = min(min_dp[j], dp[j - 1][x] - dp[j][x])

    return min(n, [min_dp[j] + j for j in range(k)])

## Structure
def min_changes(nums, k):
    # Your code here

    pass