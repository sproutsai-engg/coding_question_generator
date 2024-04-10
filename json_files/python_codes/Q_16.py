##Question ID: 16

def threeSumClosest(nums, target):
    nums.sort()
    closest = sum(nums[:3])
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum == target:
                return cur_sum
            if abs(target - cur_sum) < abs(target - closest):
                closest = cur_sum
            if cur_sum < target:
                left += 1
            else:
                right -= 1
    return closest

## Structure
def threeSumClosest(nums, target):
    # Your code here

    pass