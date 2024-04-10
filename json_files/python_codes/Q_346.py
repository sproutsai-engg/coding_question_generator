##Question ID: 346

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.maxSize = size
        self.sum = 0.0

    def next(self, val: int) -> float:
        if len(self.queue) == self.maxSize:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)

## Structure
from collections import deque
    # Your code here

    pass