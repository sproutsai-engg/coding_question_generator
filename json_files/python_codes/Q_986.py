##Question ID: 986

from itertools import permutations

def largestTimeFromDigits(arr):
    max_time = -1
    for h, i, j, k in permutations(arr):
        hour = h * 10 + i
        minute = j * 10 + k
        time = hour * 60 + minute
        if hour < 24 and minute < 60 and time > max_time:
            max_time = time

    if max_time == -1:
        return ""
    else:
        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)

## Structure
from itertools import permutations
    # Your code here

    pass