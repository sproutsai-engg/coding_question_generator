##Question ID: 323

def countComponents(n, edges):
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = [False] * n
    connected_components = 0

    def dfs(node):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            connected_components += 1

    return connected_components


## Structure
def countComponents(n, edges):
    # Your code here

    pass