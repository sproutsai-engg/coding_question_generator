def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == "__main__":
    inputs  = [[4, 5, 6, 7, 0, 1, 2], 0]
    nums = inputs[0]
    target = inputs[1]
    result = search(nums, target)
    print(result)