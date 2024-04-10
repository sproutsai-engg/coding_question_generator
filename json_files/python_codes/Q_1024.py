##Question ID: 1024

def count_and_triples(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] & nums[j] & nums[k] != 0:
                    count += 1
    return count

## Structure
def count_and_triples(nums):
    # Your code here

    pass