##Question ID: 1942

from sortedcontainers import SortedDict
from sortedcontainers import SortedSet

def smallestChair(times, targetFriend):
    events = SortedDict()
    for i, (arrival, leaving) in enumerate(times):
        events[arrival] = i
        events[leaving] = ~i

    availableChairs = SortedSet(range(len(times)))
    assignedChair = [0] * len(times)

    for time, idx in events.items():
        if idx >= 0:
            chair = availableChairs.pop(0)
            assignedChair[idx] = chair
            if idx == targetFriend:
                return chair
        else:
            availableChairs.add(assignedChair[~idx])

    return -1

## Structure
from sortedcontainers import SortedDict
    # Your code here

    pass