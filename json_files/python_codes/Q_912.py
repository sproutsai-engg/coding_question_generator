##Question ID: 912

import random
from bisect import bisect_left

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        for weight in w:
            previous = self.prefix_sum[-1] if self.prefix_sum else 0
            self.prefix_sum.append(previous + weight)

    def pickIndex(self) -> int:
        num = random.random() * self.prefix_sum[-1]
        return bisect_left(self.prefix_sum, num)

## Structure
import random
    # Your code here

    pass