##Question ID: 1586

def findMaxLength(nums):
    max_length, zeroes, ones = 0, 0, 0
    count_map = {0: -1}

    for i, num in enumerate(nums):
        if num == 0:
            zeroes += 1
        else:
            ones += 1

        if zeroes - ones not in count_map:
            count_map[zeroes - ones] = i
        else:
            max_length = max(max_length, i - count_map[zeroes - ones])

    return max_length

## Structure
def findMaxLength(nums):
    # Your code here

    pass