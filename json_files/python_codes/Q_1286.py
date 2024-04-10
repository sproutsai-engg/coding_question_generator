##Question ID: 1286

def max_sum_subsequence(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    result = 0

    for i in range(n):
        dp[i] = nums[i]
        for j in range(max(0, i - k), i):
            dp[i] = max(dp[i], dp[j] + nums[i])
        result = max(result, dp[i])

    return result

## Structure
def max_sum_subsequence(nums: List[int], k: int) -> int:
    # Your code here

    pass