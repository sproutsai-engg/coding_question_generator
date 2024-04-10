##Question ID: 958

def sortArrayByParityII(nums):
    j = 1
    for i in range(0, len(nums), 2):
        if nums[i] % 2:
            while nums[j] % 2:
                j += 2
            nums[i], nums[j] = nums[j], nums[i]
    return nums

## Structure
def sortArrayByParityII(nums):
    # Your code here

    pass