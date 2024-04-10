##Question ID: 56

def merge(intervals):
    if not intervals:
        return []

    intervals.sort()
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])

    return result

## Structure
def merge(intervals):
    # Your code here

    pass