##Question ID: 260

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

## Structure
def singleNumber(nums):
    # Your code here

    pass