##Question ID: 1037

def min_k_bit_flips(nums, k):
    n, res, flipped = len(nums), 0, 0
    change = [0] * n
    for i in range(n - k + 1):
        flipped ^= change[i]
        if nums[i] == flipped:
            res += 1
            flipped ^= 1
            if i + k < n:
                change[i + k] ^= 1
    for i in range(n - k + 1, n):
        flipped ^= change[i]
        if nums[i] == flipped:
            return -1
    return res


## Structure
def min_k_bit_flips(nums, k):
    # Your code here

    pass