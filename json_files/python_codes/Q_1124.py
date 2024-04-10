##Question ID: 1124

def longestWellPerformingInterval(hours):
    sum = 0
    longest = 0
    first_sum_index = {}

    for i, hour in enumerate(hours):
        sum += 1 if hour > 8 else -1
        if sum > 0:
            longest = i + 1
        else:
            if sum - 1 in first_sum_index:
                longest = max(longest, i - first_sum_index[sum - 1])
            if sum not in first_sum_index:
                first_sum_index[sum] = i

    return longest


## Structure
def longestWellPerformingInterval(hours):
    # Your code here

    pass