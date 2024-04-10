##Question ID: 45

def jump(nums):
    jumps = 0
    current_end = 0
    current_farthest = 0

    for i in range(len(nums) - 1):
        current_farthest = max(current_farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = current_farthest

    return jumps

## Structure
def jump(nums):
    # Your code here

    pass