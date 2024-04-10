##Question ID: 1087

def longestArithSeqLength(nums):
    n = len(nums)
    longest = 0
    dp = [{} for _ in range(n)]
    
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            longest = max(longest, dp[i][diff])
    
    return longest

## Structure
def longestArithSeqLength(nums):
    # Your code here

    pass