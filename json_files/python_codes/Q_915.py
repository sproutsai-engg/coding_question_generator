##Question ID: 915

import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        angle = random.random() * 2 * math.pi
        r = math.sqrt(random.random()) * self.radius
        return [self.x_center + r * math.cos(angle), self.y_center + r * math.sin(angle)]

## Structure
import random
    # Your code here

    pass