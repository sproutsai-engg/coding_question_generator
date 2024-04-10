##Question ID: 611

def triangleNumber(nums: list) -> int:
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] > nums[k]:
                    count += 1
                else:
                    break
    return count

## Structure
def triangleNumber(nums: list) -> int:
    # Your code here

    pass