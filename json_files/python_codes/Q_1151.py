##Question ID: 1151

def minSwaps(data):
    ones = sum(data)
    cur_ones, max_ones = 0, 0
    for i, d in enumerate(data):
        cur_ones += d
        if i >= ones:
            cur_ones -= data[i - ones]
        max_ones = max(max_ones, cur_ones)
    return ones - max_ones


## Structure
def minSwaps(data):
    # Your code here

    pass