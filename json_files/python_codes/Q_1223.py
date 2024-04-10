##Question ID: 1223

def areConnected(n, threshold, queries):
    answer = [False] * len(queries)
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def unite(x, y):
        rootx = find(x)
        rooty = find(y)
        if rootx != rooty:
            if rank[rootx] > rank[rooty]:
                rootx, rooty = rooty, rootx
            parent[rootx] = rooty
            if rank[rootx] == rank[rooty]:
                rank[rooty] += 1

    for i in range(threshold + 1, n + 1):
        for j in range(i * 2, n + 1, i):
            unite(i, j)

    for i, query in enumerate(queries):
        answer[i] = find(query[0]) == find(query[1])

    return answer

## Structure
def areConnected(n, threshold, queries):
    # Your code here

    pass