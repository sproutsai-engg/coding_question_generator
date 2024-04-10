##Question ID: 628

def maximumProduct(nums):
    nums.sort()
    n = len(nums)
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

## Structure
def maximumProduct(nums):
    # Your code here

    pass