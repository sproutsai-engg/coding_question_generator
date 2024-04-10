##Question ID: 1616

def min_difference(nums):
    size = len(nums)
    if size < 5:
        return 0

    nums.sort()

    return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])

## Structure
def min_difference(nums):
    # Your code here

    pass