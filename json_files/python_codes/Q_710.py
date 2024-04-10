##Question ID: 710

import random

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        blacklist.sort()
        self.mapping = dict()
        idx = 0
        for black in blacklist:
            while idx < black:
                self.mapping[idx] = n - 1
                idx += 1
                n -= 1
            idx += 1
            n -= 1
        self.last = n

    def pick(self) -> int:
        num = random.randrange(self.last)
        return self.mapping.get(num, num)

## Structure
import random
    # Your code here

    pass