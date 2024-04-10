##Question ID: 78

def subsets(nums):
    n = len(nums)
    num_subsets = 1 << n
    result = []

    for i in range(num_subsets):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)
    return result

## Structure
def subsets(nums):
    # Your code here

    pass