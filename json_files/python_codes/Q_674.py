##Question ID: 674

def findLengthOfLCIS(nums):
    if not nums:
        return 0
    result, current = 1, 1
    for i in range(1, len(nums)):
        current = current + 1 if nums[i] > nums[i - 1] else 1
        result = max(result, current)
    return result

## Structure
def findLengthOfLCIS(nums):
    # Your code here

    pass