##Question ID: 352

from collections import OrderedDict

class SummaryRanges:

    def __init__(self):
        self.intervals = OrderedDict()

    def addNum(self, val: int) -> None:
        if not self.intervals or next(iter(self.intervals)) > val + 1:
            self.intervals[val] = val
        else:
            keys = list(self.intervals.keys())
            idx = bisect_left(keys, val)
            if idx > 0 and keys[idx - 1] <= val <= self.intervals[keys[idx - 1]]:
                pass
            elif idx < len(keys) and val + 1 == keys[idx]:
                self.intervals[val] = self.intervals[keys[idx]]
                del self.intervals[keys[idx]]
            else:
                self.intervals[val] = val

    def getIntervals(self):
        return list(self.intervals.items())


## Structure
from collections import OrderedDict
    # Your code here

    pass