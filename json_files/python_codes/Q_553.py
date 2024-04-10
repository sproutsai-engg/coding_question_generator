##Question ID: 553

def optimal_division(nums):
    n = len(nums)
    if n == 1:
        return str(nums[0])
    if n == 2:
        return str(nums[0]) + '/' + str(nums[1])
    res = str(nums[0]) + '/('
    for i in range(1, n - 1):
        res += str(nums[i]) + '/'
    res += str(nums[n - 1]) + ')'
    return res


## Structure
def optimal_division(nums):
    # Your code here

    pass