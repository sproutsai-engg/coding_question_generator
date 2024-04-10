##Question ID: 1878

def check(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            count += 1
        if count > 1:
            return False
    return count == 1 or nums[0] >= nums[-1]

## Structure
def check(nums):
    # Your code here

    pass