##Question ID: 1548

def kLengthApart(nums, k):
    last_one = -1
    for i, num in enumerate(nums):
        if num == 1:
            if last_one != -1 and i - last_one <= k:
                return False
            last_one = i
    return True

## Structure
def kLengthApart(nums, k):
    # Your code here

    pass