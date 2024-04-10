##Question ID: 503

def nextGreaterElements(nums):
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums) * 2):
        index = i % len(nums)
        while stack and nums[stack[-1]] < nums[index]:
            result[stack.pop()] = nums[index]
        if i < len(nums):
            stack.append(index)

    return result

## Structure
def nextGreaterElements(nums):
    # Your code here

    pass