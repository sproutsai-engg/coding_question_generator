##Question ID: 53

def maxSubArray(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum

## Structure
def maxSubArray(nums):
    # Your code here

    pass