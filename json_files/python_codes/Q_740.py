##Question ID: 740

def max_points(nums):
    dp = [0] * 100001
    max_points = 0
    for num in nums:
        dp[num] += 1
    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 1], dp[i - 2] + i * dp[i])
        max_points = max(max_points, dp[i])
    return max_points

## Structure
def max_points(nums):
    # Your code here

    pass