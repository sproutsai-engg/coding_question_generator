##Question ID: 1344

def maxEqualFreq(nums):
    count, freq = {}, {}
    max_len, max_freq = 0, 0
    for i, num in enumerate(nums):
        count[num] = count.get(num, 0) + 1
        freq[count[num] - 1] = freq.get(count[num] - 1, 0) - 1
        freq[count[num]] = freq.get(count[num], 0) + 1

        max_freq = max(max_freq, count[num])
        if max_freq * (i + 1) == i or max_freq * (freq.get(max_freq - 1, 0) + 1) + (max_freq - 1) * freq.get(max_freq - 1, 0) == i:
            max_len = i + 1
    return max_len


## Structure
def maxEqualFreq(nums):
    # Your code here

    pass