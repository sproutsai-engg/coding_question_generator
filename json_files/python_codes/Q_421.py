##Question ID: 421

def findMaximumXOR(nums):
    max_xor = 0
    mask = 0

    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = {num & mask for num in nums}

        possible_max = max_xor | (1 << i)

        for prefix in prefixes:
            if prefix ^ possible_max in prefixes:
                max_xor = possible_max
                break

    return max_xor

## Structure
def findMaximumXOR(nums):
    # Your code here

    pass