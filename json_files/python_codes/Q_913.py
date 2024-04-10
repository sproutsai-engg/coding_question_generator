##Question ID: 913

import random

class Solution:
    def __init__(self, m, n):
        self.grid = [[0] * n for _ in range(m)]
        self.zero_count = m * n

    def pick(self):
        index = random.randrange(self.zero_count)

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    if index == 0:
                        self.grid[i][j] = 1
                        self.zero_count -= 1
                        return (i, j)
                    index -= 1
        return (-1, -1)  # Should not happen

## Structure
import random
    # Your code here

    pass