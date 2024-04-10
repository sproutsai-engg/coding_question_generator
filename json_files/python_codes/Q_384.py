##Question ID: 384

import random

class Solution:
    def __init__(self, nums):
        self.original = nums

    def reset(self):
        return self.original

    def shuffle(self):
        shuffled = self.original[:]
        for i in range(len(shuffled) - 1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled


## Structure
import random
    # Your code here

    pass