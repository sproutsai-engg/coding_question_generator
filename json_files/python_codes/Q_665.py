##Question ID: 665

def checkPossibility(nums):
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            cnt += 1
            if i == 1 or nums[i] >= nums[i - 2]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i - 1]
            if cnt > 1:
                return False
    return True

## Structure
def checkPossibility(nums):
    # Your code here

    pass