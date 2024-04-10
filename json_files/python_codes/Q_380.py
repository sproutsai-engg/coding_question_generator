##Question ID: 380

import random

class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.index_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        last = self.nums[-1]
        self.index_map[last] = self.index_map[val]
        self.nums[self.index_map[val]] = last

        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]

## Structure
import random
    # Your code here

    pass