##Question ID: 644

def findMaxAverage(nums, k):
    total = sum(nums[:k])
    max_avg = total / k
    for i in range(k, len(nums)):
        total += nums[i] - nums[i - k]
        max_avg = max(max_avg, total / k)
    return max_avg

## Structure
def findMaxAverage(nums, k):
    # Your code here

    pass