##Question ID: 1870

from math import ceil

def minSpeedOnTime(dist, hour):
    max_time = hour - len(dist) + 1
    lower, upper = 1.0, 1e7
    while upper - lower >= 1e-9:
        mid = (lower + upper) / 2
        time_taken = sum(ceil(d / mid) - (0 if i == len(dist) - 1 else 1) for i, d in enumerate(dist))
        if time_taken <= max_time:
            upper = mid
        else:
            lower = mid
    return ceil(lower) if lower <= 1e7 else -1

## Structure
from math import ceil
    # Your code here

    pass