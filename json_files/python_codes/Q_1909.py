##Question ID: 1909

def canBeIncreasing(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            count += 1
            if count > 1: return False
            if i > 1 and nums[i - 2] >= nums[i] and i < len(nums) - 1 and nums[i - 1] >= nums[i + 1]: return False
    return True

## Structure
def canBeIncreasing(nums):
    # Your code here

    pass