##Question ID: 1738

def maximalNetworkRank(n, roads):
    degree = [0] * n
    s = set()
    
    for road in roads:
        degree[road[0]] += 1
        degree[road[1]] += 1
        s.add(tuple(sorted(road)))
    
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, degree[i] + degree[j] - (1 if (i, j) in s else 0))
    return ans


## Structure
def maximalNetworkRank(n, roads):
    # Your code here

    pass