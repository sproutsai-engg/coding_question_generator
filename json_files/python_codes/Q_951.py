##Question ID: 951

def partitionDisjoint(nums):
    left_max, global_max, left_length = nums[0], nums[0], 1
    for i in range(1, len(nums)):
        if nums[i] < left_max:
            left_max = global_max
            left_length = i + 1
        else:
            global_max = max(global_max, nums[i])
    return left_length

## Structure
def partitionDisjoint(nums):
    # Your code here

    pass