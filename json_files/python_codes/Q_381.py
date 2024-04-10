##Question ID: 381

import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.indices = defaultdict(set)
        self.nums = []

    def insert(self, val):
        self.nums.append(val)
        self.indices[val].add(len(self.nums) - 1)
        return len(self.indices[val]) == 1

    def remove(self, val):
        if not self.indices[val]:
            return False

        idx = self.indices[val].pop()
        if idx < len(self.nums) - 1:
            last = self.nums[-1]
            self.nums[idx] = last
            self.indices[last].remove(len(self.nums) - 1)
            self.indices[last].add(idx)
        self.nums.pop()
        return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]


## Structure
import random
    # Your code here

    pass