##Question ID: 1664

def numberOfFairs(nums):
    even_sum = sum(nums[0::2])
    odd_sum = sum(nums[1::2])
    l_even = l_odd = count = 0
    for i, num in enumerate(nums):
        if i % 2 == 0:
            even_sum -= num
            if l_even + odd_sum == l_odd + even_sum:
                count += 1
            l_even += num
        else:
            odd_sum -= num
            if l_even + odd_sum == l_odd + even_sum:
                count += 1
            l_odd += num
    return count

## Structure
def numberOfFairs(nums):
    # Your code here

    pass