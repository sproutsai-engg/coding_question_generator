##Question ID: 946

def minimum_score(nums, k):
    nums.sort()
    n = len(nums)
    res = nums[n - 1] - nums[0]

    for i in range(n - 1):
        high = max(nums[i] + k, nums[n - 1] - k)
        low = min(nums[i + 1] - k, nums[0] + k)
        res = min(res, high - low)

    return res

## Structure
def minimum_score(nums, k):
    # Your code here

    pass