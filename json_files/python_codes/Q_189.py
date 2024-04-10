##Question ID: 189

def rotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]

## Structure
def rotate(nums, k):
    # Your code here

    pass