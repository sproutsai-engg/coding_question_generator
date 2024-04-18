def twoSum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i
    return []


if __name__ == "__main__":
    inputs =  [[3, 2, 4], 6]
    nums = inputs[0]
    target = inputs[1]
    result = twoSum(nums, target)
    print(result)