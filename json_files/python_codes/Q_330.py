##Question ID: 330

def minPatches(nums, n):
    max_sum = 0
    patches = 0
    i = 0

    while max_sum < n:
        if i < len(nums) and nums[i] <= max_sum + 1:
            max_sum += nums[i]
            i += 1
        else:
            max_sum += max_sum + 1
            patches += 1

    return patches


## Structure
def minPatches(nums, n):
    # Your code here

    pass