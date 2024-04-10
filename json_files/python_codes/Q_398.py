##Question ID: 398

import random

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        count, res = 0, 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(0, count - 1) == 0:
                    res = i
        return res

## Structure
import random
    # Your code here

    pass