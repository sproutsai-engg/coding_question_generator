##Question ID: 462

def min_moves2(nums):
    nums.sort()
    mid = nums[len(nums) // 2]
    moves = 0
    for num in nums:
        moves += abs(num - mid)
    return moves

## Structure
def min_moves2(nums):
    # Your code here

    pass