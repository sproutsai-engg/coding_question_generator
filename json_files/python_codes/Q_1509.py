##Question ID: 1509

def minDifference(nums):
    n = len(nums)
    if n <= 4: return 0
    nums.sort()
    res = float('inf')
    for i in range(4):
        res = min(res, nums[n - 4 + i] - nums[i])
    return res

## Structure
def minDifference(nums):
    # Your code here

    pass