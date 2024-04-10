##Question ID: 565

def arrayNesting(nums):
    n = len(nums)
    max_len = 0
    for i in range(n):
        if nums[i] != -1:
            start = nums[i]
            count = 0
            while nums[start] != -1:
                temp = start
                start = nums[start]
                count += 1
                nums[temp] = -1
            max_len = max(max_len, count)
    return max_len

## Structure
def arrayNesting(nums):
    # Your code here

    pass