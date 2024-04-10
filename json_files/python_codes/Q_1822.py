##Question ID: 1822

def signFunc(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def arraySign(nums):
    product = 1
    for num in nums:
        product *= signFunc(num)
    return product

## Structure
def signFunc(x):
    # Your code here

    pass