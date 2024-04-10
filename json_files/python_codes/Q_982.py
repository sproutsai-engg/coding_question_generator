##Question ID: 982

def min_moves_unique(nums):
    nums.sort()
    moves = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            diff = nums[i - 1] - nums[i] + 1
            moves += diff
            nums[i] += diff
    return moves

## Structure
def min_moves_unique(nums):
    # Your code here

    pass