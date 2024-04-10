##Question ID: 643

def findMaxAverage(nums, k):
    n = len(nums)
    sum_ = sum(nums[:k])
    max_avg = sum_ / k
    for i in range(k, n):
        sum_ = sum_ - nums[i - k] + nums[i]
        max_avg = max(max_avg, sum_ / k)
    return max_avg

## Structure
def findMaxAverage(nums, k):
    # Your code here

    pass