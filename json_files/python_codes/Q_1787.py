##Question ID: 1787

def calculate_summation_of_absolute_differences(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                result[i] += abs(nums[i] - nums[j])

    return result

## Structure
def calculate_summation_of_absolute_differences(nums):
    # Your code here

    pass