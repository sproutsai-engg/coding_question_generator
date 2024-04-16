def singleNumber(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num

    bit = xor_all & -xor_all
    n1 = 0
    n2 = 0
    for num in nums:
        if num & bit:
            n1 ^= num
        else:
            n2 ^= num

    return n1, n2


if __name__ == "__main__":
    nums =[4, 2, 4, 6, 2, 1]
    result = singleNumber(nums)
    print(result)