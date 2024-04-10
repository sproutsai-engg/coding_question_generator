##Question ID: 1478

def max_events(events):
    events.sort(key=lambda x: x[1])

    count = 0
    last_day = -1

    for event in events:
        if event[0] > last_day:
            count += 1
            last_day = event[1]

    return count

## Structure
def max_events(events):
    # Your code here

    pass