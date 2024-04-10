##Question ID: 1798

def maxOperations(nums, k):
    count = {}
    operations = 0

    for num in nums:
        if count.get(k - num, 0) > 0:
            count[k - num] -= 1
            operations += 1
        else:
            count[num] = count.get(num, 0) + 1

    return operations


## Structure
def maxOperations(nums, k):
    # Your code here

    pass