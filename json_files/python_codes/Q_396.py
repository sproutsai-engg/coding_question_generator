##Question ID: 396

def maxRotateFunction(nums):
    n = len(nums)
    total_sum = sum(nums)
    f = sum(i * num for i, num in enumerate(nums))

    max_f = f
    for i in range(1, n):
        f += total_sum - n * nums[-i]
        max_f = max(max_f, f)

    return max_f


## Structure
def maxRotateFunction(nums):
    # Your code here

    pass