##Question ID: 828

def xor_game(nums: List[int]) -> bool:
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    return xor_sum == 0 or len(nums) % 2 == 0

## Structure
def xor_game(nums: List[int]) -> bool:
    # Your code here

    pass