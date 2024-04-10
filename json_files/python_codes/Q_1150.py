##Question ID: 1150

def is_majority_element(nums, target):
    count = 0
    for num in nums:
        if num == target: count += 1
        if count > len(nums) / 2: return True
    return False

## Structure
def is_majority_element(nums, target):
    # Your code here

    pass