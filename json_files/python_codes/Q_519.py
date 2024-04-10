##Question ID: 519

import random

class Solution:
    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n
        self.matrix = [[0] * n for _ in range(m)]

    def flip(self):
        idx = random.randint(0, self.total - 1)
        self.total -= 1

        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] == 0:
                    if idx == 0:
                        self.matrix[i][j] = 1
                        return [i, j]
                    idx -= 1
        return [-1, -1] # This line should never be reached

    def reset(self):
        self.total = self.m * self.n
        for row in self.matrix:
            for j in range(self.n):
                row[j] = 0


## Structure
import random
    # Your code here

    pass