##Question ID: 55

def canJump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True

## Structure
def canJump(nums):
    # Your code here

    pass