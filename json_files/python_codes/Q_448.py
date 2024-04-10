##Question ID: 448

def find_disappeared_numbers(nums):
    result = []
    
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])

    for i, num in enumerate(nums):
        if num > 0:
            result.append(i + 1)

    return result

## Structure
def find_disappeared_numbers(nums):
    # Your code here

    pass