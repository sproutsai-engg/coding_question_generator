##Question ID: 732

from collections import defaultdict
import heapq

class MyCalendarThree:

    def __init__(self):
        self.timeline = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        ongoing, k = 0, 0
        for value in self.timeline.values():
            k = max(k, ongoing + value)
            ongoing += value
        return k


## Structure
from collections import defaultdict
    # Your code here

    pass