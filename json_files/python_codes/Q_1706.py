##Question ID: 1706

def minCostConnectPoints(points):
    n = len(points)
    cost = [float('inf')] * n
    visited = [False] * n
    cost[0] = 0

    ans = 0

    for _ in range(n):
        min_cost = float('inf')
        cur_point = -1
        for j in range(n):
            if not visited[j] and cost[j] < min_cost:
                min_cost = cost[j]
                cur_point = j

        visited[cur_point] = True
        ans += min_cost

        for j in range(n):
            if not visited[j]:
                new_cost = abs(points[cur_point][0] - points[j][0]) + abs(points[cur_point][1] - points[j][1])
                cost[j] = min(cost[j], new_cost)

    return ans


## Structure
def minCostConnectPoints(points):
    # Your code here

    pass