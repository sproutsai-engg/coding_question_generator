##Question ID: 495

def find_poisoned_duration(time_series, duration):
    if not time_series:
        return 0
    total = 0
    for i in range(1, len(time_series)):
        total += min(time_series[i] - time_series[i - 1], duration)
    return total + duration

## Structure
def find_poisoned_duration(time_series, duration):
    # Your code here

    pass