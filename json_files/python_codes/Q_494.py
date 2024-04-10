##Question ID: 494

def findTargetSumWays(nums, target):
    total_sum = sum(nums)
    if total_sum < target or (total_sum + target) % 2 != 0:
        return 0
    target_sum = (total_sum + target) // 2
    dp = [0] * (target_sum + 1)
    dp[0] = 1
    for num in nums:
        for j in range(target_sum, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[target_sum]


## Structure
def findTargetSumWays(nums, target):
    # Your code here

    pass