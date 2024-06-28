def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


import torch
if __name__ == "__main__":
    nums = [3, 4, -1, 1]
    result = firstMissingPositive(nums)
    print("$sprouts@pankaj",result,"$sprouts@pankaj")    