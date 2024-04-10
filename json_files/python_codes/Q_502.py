##Question ID: 502

import heapq

def findMaximizedCapital(k: int, w: int, profits, capital) -> int:
    project_pool = list(zip(capital, profits))
    project_pool.sort(reverse=True)
    
    profit_pool = []
    
    while k:
        while project_pool and project_pool[-1][0] <= w:
            heapq.heappush(profit_pool, -project_pool.pop()[1])
        
        if not profit_pool:
            break
        
        w -= heapq.heappop(profit_pool)
        k -= 1
        
    return w

## Structure
import heapq
    # Your code here

    pass