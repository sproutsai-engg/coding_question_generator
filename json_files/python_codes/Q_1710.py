##Question ID: 1710

import heapq

def busiest_servers(k, arrival, load):
    server_requests = [0] * k
    pq = []
    available_servers = list(range(k))

    for i in range(len(arrival)):
        while pq and pq[0][0] <= arrival[i]:
            _, server_id = heapq.heappop(pq)
            available_servers.append(server_id)

        if available_servers:
            server_id = available_servers.pop(0)
            server_requests[server_id] += 1
            heapq.heappush(pq, (arrival[i] + load[i], server_id))

    max_requests = max(server_requests)
    return [i for i in range(k) if server_requests[i] == max_requests]


## Structure
import heapq
    # Your code here

    pass