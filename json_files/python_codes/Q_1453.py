##Question ID: 1453

def numPoints(darts, r):
    n = len(darts)
    result = 1
    
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(n):
                dx = darts[i][0] - darts[k][0]
                dy = darts[i][1] - darts[k][1]
                if (dx * dx + dy * dy) ** 0.5 <= r:
                    cnt += 1
                    
            if cnt > result:
                result = cnt
                
    return result

## Structure
def numPoints(darts, r):
    # Your code here

    pass