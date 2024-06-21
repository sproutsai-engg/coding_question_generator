def findMaxConsecutiveOnes(nums):
    max_consecutive, current_consecutive = 0, 0
    for num in nums:
        current_consecutive = current_consecutive + 1 if num == 1 else 0
        max_consecutive = max(max_consecutive, current_consecutive)
    return max_consecutive


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1, 1]
    result = findMaxConsecutiveOnes(nums)
    print(result)