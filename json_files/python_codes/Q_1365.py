##Question ID: 1365

def smallerNumbersThanCurrent(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result

## Structure
def smallerNumbersThanCurrent(nums):
    # Your code here

    pass