##Question ID: 1482

def smallerNumbersThanCurrent(nums):
    result = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                result[i] += 1
    return result

## Structure
def smallerNumbersThanCurrent(nums):
    # Your code here

    pass