##Question ID: 1514

def min_start_value(nums):
    min_sum, sum = 0, 0
    for num in nums:
        sum += num
        min_sum = min(min_sum, sum)
    return 1 - min_sum

## Structure
def min_start_value(nums):
    # Your code here

    pass