##Question ID: 1849

def maxAbsoluteSum(nums):
    max_sum, min_sum, max_so_far, min_so_far = 0, 0, 0, 0
    for num in nums:
        max_so_far = max(num, max_so_far + num)
        max_sum = max(max_sum, max_so_far)

        min_so_far = min(num, min_so_far + num)
        min_sum = min(min_sum, min_so_far)
    return max(max_sum, abs(min_sum))

## Structure
def maxAbsoluteSum(nums):
    # Your code here

    pass