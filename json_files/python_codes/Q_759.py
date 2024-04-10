##Question ID: 759

def min_set_size(intervals):
    intervals.sort()
    n = len(intervals)
    end = intervals[0][1]
    count = 1

    for i in range(1, n):
        if end < intervals[i][0]:
            end = intervals[i][1]
            count += 1
        else:
            end = min(end, intervals[i][1])
    return count * 2

## Structure
def min_set_size(intervals):
    # Your code here

    pass