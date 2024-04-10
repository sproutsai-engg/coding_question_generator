##Question ID: 377

def combination_sum(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for i in range(num, target + 1):
            dp[i] += dp[i - num]

    return dp[target]


## Structure
def combination_sum(nums, target):
    # Your code here

    pass