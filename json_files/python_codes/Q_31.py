##Question ID: 31

def nextPermutation(nums):
    n, k = len(nums), -1
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            k = i - 1
            break
    if k == -1:
        nums.reverse()
    else:
        l = 0
        for i in range(n - 1, k, -1):
            if nums[i] > nums[k]:
                l = i
                break
        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1:] = reversed(nums[k + 1:])

## Structure
def nextPermutation(nums):
    # Your code here

    pass