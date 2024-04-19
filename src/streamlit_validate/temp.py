def twoSum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i
    return []


if __name__ == "__main__":
    inputs = [[1, 2, 3, 4, 5], 9]
    nums = inputs[0]
    target = inputs[1]
    result = twoSum(nums, target)
    print(result)