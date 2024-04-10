##Question ID: 778

import heapq

def rearrange_string(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    
    pq = [(-count, char) for char, count in counts.items()]
    heapq.heapify(pq)
    
    result = []
    previous = (0, '')
    
    while pq:
        count, char = heapq.heappop(pq)
        result.append(char)
        
        if previous[0] < 0:
            heapq.heappush(pq, previous)
        
        count += 1
        previous = (count, char)
    
    result_str = ''.join(result)
    return result_str if len(result_str) == len(s) else ""


## Structure
import heapq
    # Your code here

    pass