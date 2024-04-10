##Question ID: 645

def findErrorNums(nums):
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
        else:
            result.append(index + 1)
    for i, num in enumerate(nums):
        if num > 0:
            result.append(i + 1)
            break
    return result

## Structure
def findErrorNums(nums):
    # Your code here

    pass