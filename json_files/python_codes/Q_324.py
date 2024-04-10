##Question ID: 324

def wiggleSort(nums):
    nums.sort()
    for i in range(1, len(nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]


## Structure
def wiggleSort(nums):
    # Your code here

    pass