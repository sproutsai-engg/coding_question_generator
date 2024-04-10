##Question ID: 1247

def moves_to_make_zigzag(nums):
    moves1, moves2 = 0, 0
    for i in range(len(nums)):
        left = nums[i - 1] if i > 0 else float('inf')
        right = nums[i + 1] if i + 1 < len(nums) else float('inf')
        diff1 = nums[i] - min(left, right) + 1
        diff2 = nums[i] - min(left, right) + 1
        if i % 2 == 0:
            moves1 += max(0, diff1)
        else:
            moves2 += max(0, diff2)
    return min(moves1, moves2)

## Structure
def moves_to_make_zigzag(nums):
    # Your code here

    pass