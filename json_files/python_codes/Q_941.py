##Question ID: 941

def move_even_odd(nums):
    even_index = 0
    odd_index = len(nums) - 1

    while even_index < odd_index:
        if nums[even_index] % 2 == 0:
            even_index += 1
        else:
            nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
            odd_index -= 1

    return nums

## Structure
def move_even_odd(nums):
    # Your code here

    pass