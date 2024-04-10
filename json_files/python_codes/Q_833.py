##Question ID: 833

from collections import defaultdict
from queue import Queue

def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    stop_to_buses = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].add(i)

    q = Queue()
    visited_buses = set()
    num_buses = 0
    q.put(source)

    while not q.empty():
        size = q.qsize()
        for _ in range(size):
            stop = q.get()
            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return num_buses + 1
                    q.put(next_stop)
        num_buses += 1

    return -1

## Structure
from collections import defaultdict
    # Your code here

    pass