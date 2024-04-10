##Question ID: 630

import heapq

def scheduleCourse(courses):
    courses.sort(key=lambda x: x[1])
    curr_time, duration_sum = 0, []

    for duration, deadline in courses:
        curr_time += duration
        heapq.heappush(duration_sum, -duration)

        if curr_time > deadline:
            curr_time += heapq.heappop(duration_sum)

    return len(duration_sum)

## Structure
import heapq
    # Your code here

    pass