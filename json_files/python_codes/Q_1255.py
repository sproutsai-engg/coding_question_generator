##Question ID: 1255

def maxValueAfterReverse(nums):
    total, diff = 0, 0
    min2, max2 = float('inf'), float('-inf')
    for i in range(len(nums) - 1):
        total += abs(nums[i] - nums[i + 1])
        min2 = min(min2, max(nums[i], nums[i + 1]))
        max2 = max(max2, min(nums[i], nums[i + 1]))
        diff = max(diff, abs(nums[i + 1] - nums[0]) - abs(nums[i + 1] - nums[i]))
        diff = max(diff, abs(nums[i] - nums[-1]) - abs(nums[i] - nums[i + 1]))
    return total + max(diff, 2 * (max2 - min2))

## Structure
def maxValueAfterReverse(nums):
    # Your code here

    pass