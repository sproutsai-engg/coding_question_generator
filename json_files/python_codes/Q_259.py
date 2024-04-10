##Question ID: 259

def threeSumSmaller(nums, target):
    count = 0
    nums.sort()
    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] < target:
                count += k - j
                j += 1
            else:
                k -= 1
    return count

## Structure
def threeSumSmaller(nums, target):
    # Your code here

    pass