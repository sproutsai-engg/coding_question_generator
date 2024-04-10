##Question ID: 1388

def maxSumDivThree(nums):
    dp = [0, 0, 0]
    for num in nums:
        temp = dp[:]
        for s in temp:
            dp[(s + num) % 3] = max(dp[(s + num) % 3], s + num)
    return dp[0]

## Structure
def maxSumDivThree(nums):
    # Your code here

    pass