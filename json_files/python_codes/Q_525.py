##Question ID: 525

def findMaxLength(nums):
    counts = {0: -1}
    max_len = count = 0
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count in counts:
            max_len = max(max_len, i - counts[count])
        else:
            counts[count] = i
    return max_len

## Structure
def findMaxLength(nums):
    # Your code here

    pass