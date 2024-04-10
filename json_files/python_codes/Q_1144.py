##Question ID: 1144

def movesToMakeZigzag(nums):
    even_moves, odd_moves = 0, 0
    for i in range(len(nums)):
        left = nums[i - 1] if i > 0 else 1001
        right = nums[i + 1] if i < len(nums) - 1 else 1001
        min_value = min(left, right)
        if nums[i] >= min_value:
            if i % 2 == 0:
                even_moves += nums[i] - min_value + 1
            else:
                odd_moves += nums[i] - min_value + 1
    return min(even_moves, odd_moves)

## Structure
def movesToMakeZigzag(nums):
    # Your code here

    pass