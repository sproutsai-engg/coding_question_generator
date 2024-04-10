##Question ID: 554

from collections import defaultdict

def least_bricks(wall):
    edge_count = defaultdict(int)
    max_count = 0

    for row in wall:
        edge_position = 0
        for i in range(len(row) - 1):
            edge_position += row[i]
            edge_count[edge_position] += 1
            max_count = max(max_count, edge_count[edge_position])

    return len(wall) - max_count


## Structure
from collections import defaultdict
    # Your code here

    pass