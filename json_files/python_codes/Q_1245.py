##Question ID: 1245

from collections import deque, defaultdict

def tree_diameter(edges):
    tree = defaultdict(list)
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    queue = deque([(0, 0)])
    furthest, max_distance = 0, 0
    while queue:
        node, distance = queue.popleft()
        if distance > max_distance:
            max_distance = distance
            furthest = node
        for neighbor in tree[node]:
            tree[neighbor].remove(node)
            queue.append((neighbor, distance + 1))

    queue.append((furthest, 0))
    max_distance = 0
    while queue:
        node, distance = queue.popleft()
        if distance > max_distance:
            max_distance = distance
        for neighbor in tree[node]:
            tree[neighbor].remove(node)
            queue.append((neighbor, distance + 1))

    return max_distance

## Structure
from collections import deque, defaultdict
    # Your code here

    pass