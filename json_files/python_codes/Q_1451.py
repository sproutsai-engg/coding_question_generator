##Question ID: 1451

def min_taps(n, ranges):
    intervals = [0] * (n + 1)
    for i in range(n + 1):
        left = max(0, i - ranges[i])
        right = min(n, i + ranges[i])
        intervals[left] = max(intervals[left], right - left)

    position, total_taps, max_reach = 0, 0, 0
    while position < n:
        max_reach = max(max_reach, position + intervals[position])
        if max_reach == position:
            return -1
        position = max_reach
        total_taps += 1

    return total_taps

## Structure
def min_taps(n, ranges):
    # Your code here

    pass