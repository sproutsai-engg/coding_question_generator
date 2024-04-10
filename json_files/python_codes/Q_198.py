##Question ID: 198

def rob(nums):
    prev1, prev2 = 0, 0
    for num in nums:
        prev1, prev2 = max(prev2 + num, prev1), prev1
    return prev1

## Structure
def rob(nums):
    # Your code here

    pass