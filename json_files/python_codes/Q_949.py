##Question ID: 949

from collections import deque

def catMouseGame(graph):
    n = len(graph)
    status = [[[0]*3 for _ in range(n)] for _ in range(n)]

    for i in range(1, n):
        status[i][i][1] = 2
        status[i][i][2] = 2
    queue = deque([(i, i, t, 2) for i in range(1, n) for t in (1, 2)])

    while queue:
        pos_m, pos_c, t_type, t_result = queue.popleft()

        for prev in graph[pos_m if t_type == 1 else pos_c]:
            if (t_type == 2 and prev == 0) or (t_result == 2 and status[prev][pos_c][3 - t_type]):
                continue
            if status[prev][pos_c][3 - t_type]:
                continue
            queue.append((pos_c, prev, 3 - t_type, 3 - t_result))
            status[prev][pos_c][3 - t_type] = 3 - t_result

    return status[1][2][1]


## Structure
from collections import deque
    # Your code here

    pass