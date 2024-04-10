##Question ID: 1222

def remove_covered_intervals(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    count = 0
    end = 0
    for i in intervals:
        if i[1] > end:
            count += 1
            end = i[1]
    return count


## Structure
def remove_covered_intervals(intervals):
    # Your code here

    pass