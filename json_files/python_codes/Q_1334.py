##Question ID: 1334

def findTheCity(n, edges, distanceThreshold):
    distance = [[1e5] * n for _ in range(n)]

    for edge in edges:
        distance[edge[0]][edge[1]] = edge[2]
        distance[edge[1]][edge[0]] = edge[2]

    for i in range(n):
        distance[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    res, minReachable = 0, n
    for i in range(n):
        reachable = sum(1 for j in range(n) if distance[i][j] <= distanceThreshold)
        if reachable <= minReachable:
            minReachable = reachable
            res = i
    return res


## Structure
def findTheCity(n, edges, distanceThreshold):
    # Your code here

    pass