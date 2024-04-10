##Question ID: 1827

def min_operations(nums):
    operations = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            operations += (nums[i - 1] - nums[i]) + 1
            nums[i] = nums[i - 1] + 1
    return operations

## Structure
def min_operations(nums):
    # Your code here

    pass