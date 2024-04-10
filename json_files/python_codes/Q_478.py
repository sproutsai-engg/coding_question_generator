##Question ID: 478

import random
from math import sqrt, pi, cos, sin

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        r = sqrt(random.random()) * self.radius
        theta = random.random() * 2 * pi
        return [self.x_center + r * cos(theta), self.y_center + r * sin(theta)]

## Structure
import random
    # Your code here

    pass