##Question ID: 169

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (num == candidate) - (num != candidate)

    return candidate

## Structure
def majority_element(nums):
    # Your code here

    pass