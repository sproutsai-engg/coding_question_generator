##Question ID: 442

def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            duplicates.append(abs(nums[i]))
        else:
            nums[index] *= -1
    return duplicates

## Structure
def find_duplicates(nums):
    # Your code here

    pass