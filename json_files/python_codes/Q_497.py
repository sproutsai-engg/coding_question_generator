##Question ID: 497

import random
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = [0] * len(rects)
        self.total_area = 0

        for i, rect in enumerate(rects):
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.areas[i] = area
            self.total_area += area

    def pick(self) -> List[int]:
        rnd = random.randint(0, self.total_area - 1)
        idx = 0
        while rnd >= self.areas[idx]:
            rnd -= self.areas[idx]
            idx += 1

        x = random.randint(self.rects[idx][0], self.rects[idx][2])
        y = random.randint(self.rects[idx][1], self.rects[idx][3])
        
        return [x, y]


## Structure
import random
    # Your code here

    pass