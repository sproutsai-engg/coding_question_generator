##Question ID: 1560

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count

## Structure
def busy_student(start_time, end_time, query_time):
    # Your code here

    pass