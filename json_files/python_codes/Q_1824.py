##Question ID: 1824

import heapq

def eatenApples(apples, days):
    n = len(apples)
    pq = []
    ans = 0

    for i in range(n + 1):
        if i < n and apples[i] > 0:
            heapq.heappush(pq, (i + days[i], apples[i]))

        while pq and pq[0][0] <= i:
            heapq.heappop(pq)

        if pq:
            ans += 1
            curr_apple = heapq.heappop(pq)
            if curr_apple[1] > 1:
                heapq.heappush(pq, (curr_apple[0], curr_apple[1] - 1))

    return ans


## Structure
import heapq
    # Your code here

    pass