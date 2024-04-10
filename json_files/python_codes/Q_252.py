##Question ID: 252

def can_attend_meetings(intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True

## Structure
def can_attend_meetings(intervals):
    # Your code here

    pass