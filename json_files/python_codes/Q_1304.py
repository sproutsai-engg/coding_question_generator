##Question ID: 1304

from heapq import heappush, heappop

def longestHappyString(a, b, c):
    res = ""
    pq = []
    if a: heappush(pq, (-a, 'a'))
    if b: heappush(pq, (-b, 'b'))
    if c: heappush(pq, (-c, 'c'))

    while pq:
        curr = heappop(pq)
        if len(res) >= 2 and res[-1] == curr[1] and res[-2] == curr[1]:
            if not pq: break
            next = heappop(pq)
            res += next[1]
            if next[0] < -1: heappush(pq, (next[0] + 1, next[1]))
            heappush(pq, curr)
        else:
            res += curr[1]
            if curr[0] < -1: heappush(pq, (curr[0] + 1, curr[1]))

    return res


## Structure
from heapq import heappush, heappop
    # Your code here

    pass