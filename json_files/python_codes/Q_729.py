##Question ID: 729

from bisect import bisect_left, insort

class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        i = bisect_left(self.calendar, [start, end])
        if i % 2 == 1:
            return False
        if i > 0 and self.calendar[i-1] > start:
            return False
        if i < len(self.calendar) and end > self.calendar[i]:
            return False
        insort(self.calendar, start)
        insort(self.calendar, end)
        return True

## Structure
from bisect import bisect_left, insort
    # Your code here

    pass