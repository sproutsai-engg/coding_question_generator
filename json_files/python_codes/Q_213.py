##Question ID: 213

def rob(nums):
    if len(nums) == 1:
        return nums[0]
    prev, curr = 0, 0
    for i in range(len(nums) - 1):
        temp = max(curr, prev + nums[i])
        prev, curr = curr, temp
    res = curr
    prev, curr = 0, 0
    for i in range(1, len(nums)):
        temp = max(curr, prev + nums[i])
        prev, curr = curr, temp
    return max(res, curr)

## Structure
def rob(nums):
    # Your code here

    pass