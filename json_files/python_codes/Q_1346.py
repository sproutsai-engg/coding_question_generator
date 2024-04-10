##Question ID: 1346

def maxValueInStack(nums, k):
    n = len(nums)
    if k >= n:
        return -1

    max_val = float('-inf')
    for i in range(k+1):
        max_val = max(max_val, nums[i])
    return max_val

## Structure
def maxValueInStack(nums, k):
    # Your code here

    pass