##Question ID: 944

def minDifference(nums, k):
    if len(nums) <= 1: return 0
    nums.sort()
    min_diff = nums[-1] - nums[0]
    for i in range(1, len(nums)):
        high = max(nums[i-1] + k, nums[-1] - k)
        low = min(nums[i] - k, nums[0] + k)
        min_diff = min(min_diff, high - low)
    return min_diff

## Structure
def minDifference(nums, k):
    # Your code here

    pass