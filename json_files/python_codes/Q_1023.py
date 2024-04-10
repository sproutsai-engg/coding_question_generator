##Question ID: 1023

from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key, value, timestamp):
        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.data: return ""
        index = bisect.bisect(self.data[key], (timestamp + 1,))
        return self.data[key][index-1][1] if index else ""

## Structure
from collections import defaultdict
    # Your code here

    pass