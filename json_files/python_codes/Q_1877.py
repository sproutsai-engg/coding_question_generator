##Question ID: 1877

def minPairSum(nums):
    nums.sort()
    max_sum = 0
    for i in range(len(nums) // 2):
        max_sum = max(max_sum, nums[i] + nums[-1 - i])
    return max_sum

## Structure
def minPairSum(nums):
    # Your code here

    pass