##Question ID: 914

import random
from bisect import bisect_left

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.areas = []
        self.total_area = 0
        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.total_area += area
            self.areas.append(self.total_area)

    def pick(self):
        random_area = random.randint(0, self.total_area - 1)
        rect_index = bisect_left(self.areas, random_area + 1)

        x = random.randint(self.rects[rect_index][0], self.rects[rect_index][2])
        y = random.randint(self.rects[rect_index][1], self.rects[rect_index][3])

        return [x, y]


## Structure
import random
    # Your code here

    pass