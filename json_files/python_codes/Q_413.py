##Question ID: 413

def numberOfArithmeticSlices(nums):
    n = len(nums)
    count, cur = 0, 0
    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            cur += 1
            count += cur
        else:
            cur = 0
    return count

## Structure
def numberOfArithmeticSlices(nums):
    # Your code here

    pass