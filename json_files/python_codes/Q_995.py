##Question ID: 995

def min_k_bit_flips(nums, k):
    n = len(nums)
    flipped = [0] * n
    flips = ans = 0
    for i in range(n):
        if i >= k:
            flips -= flipped[i - k]
        if (flips + nums[i]) % 2 == 0:
            if i + k > n:
                return -1
            flipped[i] = 1
            flips += 1
            ans += 1
    return ans

## Structure
def min_k_bit_flips(nums, k):
    # Your code here

    pass