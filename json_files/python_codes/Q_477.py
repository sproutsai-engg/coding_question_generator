##Question ID: 477

def total_hamming_distance(nums):
    total_distance = 0
    n = len(nums)

    for i in range(32):
        bit_count = sum(((num >> i) & 1) for num in nums)
        total_distance += bit_count * (n - bit_count)

    return total_distance

## Structure
def total_hamming_distance(nums):
    # Your code here

    pass