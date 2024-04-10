##Question ID: 697

def findShortestSubArray(nums):
    freq_map, start_map = {}, {}
    max_freq, min_length = 0, len(nums)

    for i, num in enumerate(nums):
        if num not in start_map:
            start_map[num] = i
        freq_map[num] = freq_map.get(num, 0) + 1

        freq = freq_map[num]
        if freq > max_freq:
            max_freq = freq
            min_length = i - start_map[num] + 1
        elif freq == max_freq:
            min_length = min(min_length, i - start_map[num] + 1)

    return min_length

## Structure
def findShortestSubArray(nums):
    # Your code here

    pass