##Question ID: 1353

import heapq

def maxEvents(events: List[List[int]]) -> int:
    events.sort(key=lambda x: x[0])
    min_heap = []
    event_count, day = 0, 0

    for event in events:
        while min_heap and min_heap[0] < event[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, event[1])
        event_count += 1
        day += 1

    return event_count


## Structure
import heapq
    # Your code here

    pass