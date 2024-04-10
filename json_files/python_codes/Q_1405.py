##Question ID: 1405

import heapq

def longest_diverse_string(a: int, b: int, c: int) -> str:
    result = ""
    pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
    heapq.heapify(pq)
    
    while pq:
        first = heapq.heappop(pq)
        if not result or result[-1] != first[1]:
            result += first[1]
            first = (first[0] + 1, first[1])
            if first[0] < 0:
                heapq.heappush(pq, first)
        elif pq:
            second = heapq.heappop(pq)
            result += second[1]
            second = (second[0] + 1, second[1])
            if second[0] < 0:
                heapq.heappush(pq, second)
            if first[0] < 0:
                heapq.heappush(pq, first)
        else:
            break
            
    return result

## Structure
import heapq
    # Your code here

    pass