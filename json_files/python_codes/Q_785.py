##Question ID: 785

def isBipartite(graph: List[List[int]]) -> bool:
    def dfs(node: int, color: int) -> bool:
        if colors[node]:
            return colors[node] == color

        colors[node] = color
        for neighbor in graph[node]:
            if not dfs(neighbor, 3 - color):
                return False

        return True

    n = len(graph)
    colors = [0] * n

    for i in range(n):
        if not colors[i] and not dfs(i, 1):
            return False

    return True

## Structure
def isBipartite(graph: List[List[int]]) -> bool:
    # Your code here

    pass