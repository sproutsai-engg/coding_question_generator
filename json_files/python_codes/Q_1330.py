##Question ID: 1330

def longestSubsequence(arr, difference):
    dp = {}
    maxLength = 0
    for num in arr:
        dp[num] = dp.get(num - difference, 0) + 1
        maxLength = max(maxLength, dp[num])
    return maxLength


## Structure
def longestSubsequence(arr, difference):
    # Your code here

    pass