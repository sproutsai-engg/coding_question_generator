##Question ID: 547

def findCircleNum(isConnected):
    def dfs(isConnected, visited, i):
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                dfs(isConnected, visited, j)

    provinces = 0
    visited = [False] * len(isConnected)
    for i in range(len(isConnected)):
        if not visited[i]:
            dfs(isConnected, visited, i)
            provinces += 1
    return provinces

## Structure
def findCircleNum(isConnected):
    # Your code here

    pass