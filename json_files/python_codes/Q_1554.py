##Question ID: 1554

def minTime(n, edges, hasApple):
    graph = {i: {} for i in range(n)}

    for a, b in edges:
        graph[a][b] = 0
        graph[b][a] = 0

    def dfs(v, parent):
        ans = 0
        for u in graph[v]:
            if u == parent:
                continue
            ans += dfs(u, v) * 2
        return ans + int(hasApple[v] or ans > 0)

    return dfs(0, -1)

## Structure
def minTime(n, edges, hasApple):
    # Your code here

    pass