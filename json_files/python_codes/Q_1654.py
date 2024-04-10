##Question ID: 1654

from collections import deque

def minimumJumps(forbidden, a, b, x):
    forbidden_positions = set(forbidden)
    q = deque([(0, 0, 0)])
    visited = {(0, 0)}
    while q:
        pos, steps, backward = q.popleft()
        if pos == x:
            return steps
        forward_pos = pos + a
        backward_pos = pos - b
        if forward_pos <= 6000 and forward_pos not in forbidden_positions and (forward_pos, 0) not in visited:
            visited.add((forward_pos, 0))
            q.append((forward_pos, steps + 1, 0))
        if backward == 0 and backward_pos > 0 and backward_pos not in forbidden_positions and (backward_pos, 1) not in visited:
            visited.add((backward_pos, 1))
            q.append((backward_pos, steps + 1, 1))
    return -1

## Structure
from collections import deque
    # Your code here

    pass