##Question ID: 1882

import heapq
from typing import List

def assignTasks(servers: List[int], tasks: List[int]) -> List[int]:
    free_servers = [(servers[i], i) for i in range(len(servers))]
    heapq.heapify(free_servers)
    busy_servers = []
    result = [0] * len(tasks)

    for time in range(len(tasks)):
        while busy_servers and busy_servers[0][0] <= time:
            _, server_elem = heapq.heappop(busy_servers)
            heapq.heappush(free_servers, server_elem)
        
        if free_servers:
            server_elem = heapq.heappop(free_servers)
            result[time] = server_elem[1]
            heapq.heappush(busy_servers, (time + tasks[time], server_elem))

    return result


## Structure
import heapq
    # Your code here

    pass