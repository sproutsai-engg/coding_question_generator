##Question ID: 1749

def maxAbsoluteSum(nums):
    max_sum = max_end = min_sum = min_end = 0
    for num in nums:
        max_end = max(max_end + num, num)
        min_end = min(min_end + num, num)
        max_sum = max(max_sum, max_end)
        min_sum = min(min_sum, min_end)
    return max(max_sum, -min_sum)

## Structure
def maxAbsoluteSum(nums):
    # Your code here

    pass