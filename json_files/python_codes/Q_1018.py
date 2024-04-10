##Question ID: 1018

def largestPerimeter(nums):
    nums.sort(reverse=True)

    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            return nums[i] + nums[i + 1] + nums[i + 2]

    return 0

## Structure
def largestPerimeter(nums):
    # Your code here

    pass