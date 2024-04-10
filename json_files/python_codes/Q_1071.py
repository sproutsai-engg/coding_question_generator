##Question ID: 1071

def prefixesDivBy5(nums):
    result = []
    current = 0
    for num in nums:
        current = ((current << 1) | num) % 5
        result.append(current == 0)
    return result

## Structure
def prefixesDivBy5(nums):
    # Your code here

    pass