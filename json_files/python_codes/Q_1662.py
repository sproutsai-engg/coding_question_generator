##Question ID: 1662

def min_num_operations(nums):
    result = 0
    highest_bit = [0] * 32
    for num in nums:
        for j in range(32):
            if num & (1 << j):
                highest_bit[j] += 1
    for count in highest_bit:
        result = max(result, count)
    return result + 31

## Structure
def min_num_operations(nums):
    # Your code here

    pass