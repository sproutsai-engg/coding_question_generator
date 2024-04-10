##Question ID: 931

from collections import defaultdict, deque

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)

    def push(self, x: int):
        freq = self.freq[x] = self.freq[x] + 1
        self.group[freq].append(x)

    def pop(self) -> int:
        max_freq = max(self.group)
        x = self.group[max_freq].pop()
        self.freq[x] -= 1
        if not self.group[max_freq]:
            del self.group[max_freq]
        return x


## Structure
from collections import defaultdict, deque
    # Your code here

    pass