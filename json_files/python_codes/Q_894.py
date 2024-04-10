##Question ID: 894

import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist_map = {}
        self.reduced_n = n - len(blacklist)

        for b in blacklist:
            if b < n:
                self.blacklist_map[b] = -1

        for b in blacklist:
            if b >= self.reduced_n:
                continue
            while n - 1 in self.blacklist_map:
                n -= 1
            self.blacklist_map[b] = n - 1
            n -= 1

    def pick(self) -> int:
        random_int = random.randint(0, self.reduced_n - 1)
        return self.blacklist_map.get(random_int, random_int)

## Structure
import random
    # Your code here

    pass