##Question ID: 815

from collections import defaultdict, deque

def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    stop_route_map = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_route_map[stop].add(i)

    queue = deque([source])
    visited_sources = {source}

    transfers = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()
            if curr == target:
                return transfers

            for route in stop_route_map[curr]:
                for stop in routes[route]:
                    if stop not in visited_sources:
                        queue.append(stop)
                        visited_sources.add(stop)
                stop_route_map[curr].remove(route)
        transfers += 1
    return -1

## Structure
from collections import defaultdict, deque
    # Your code here

    pass