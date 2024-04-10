##Question ID: 902

import heapq

def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    i, stops, curFuel = 0, 0, startFuel
    pq = []
    while curFuel < target:
        while i < len(stations) and stations[i][0] <= curFuel:
            heapq.heappush(pq, -stations[i][1])
            i += 1
        if not pq: return -1
        curFuel += -heapq.heappop(pq)
        stops += 1
    return stops


## Structure
import heapq
    # Your code here

    pass