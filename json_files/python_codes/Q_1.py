##Question ID: 1

def twoSum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i
    return []

## Structure
def twoSum(nums, target):
    # Your code here

    pass##Question ID: 1

def twoSum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i
    return []

## Structure
def twoSum(nums, target):
    # Your code here

    pass