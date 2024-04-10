##Question ID: 1488

def get_power(x):
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        steps += 1
    return steps

def sort_by_power(lo, hi, k):
    nums = [(get_power(i), i) for i in range(lo, hi + 1)]
    nums.sort()
    return nums[k - 1][1]

## Structure
def get_power(x):
    # Your code here

    pass