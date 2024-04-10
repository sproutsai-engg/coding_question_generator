##Question ID: 436

def findRightInterval(intervals):
    starts = {interval[0]: index for index, interval in enumerate(intervals)}
    res = []

    for interval in intervals:
        right = min(filter(lambda x: x >= interval[1], starts.keys()), default=-1)
        res.append(starts[right] if right != -1 else -1)

    return res

## Structure
def findRightInterval(intervals):
    # Your code here

    pass