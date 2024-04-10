##Question ID: 1456

def findTheCity(n, edges, distanceThreshold):
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for fr, to, w in edges:
        dist[fr][to] = dist[to][fr] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    res, minReachable = -1, n + 1
    for i in range(n):
        cnt = sum(1 for d in dist[i] if d <= distanceThreshold)
        if cnt <= minReachable:
            minReachable = cnt
            res = i

    return res


## Structure
def findTheCity(n, edges, distanceThreshold):
    # Your code here

    pass