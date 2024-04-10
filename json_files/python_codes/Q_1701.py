##Question ID: 1701

def maxNumEdgesToRemove(n, edges):
    def find(u):
        if parent[u] == u:
            return u
        else:
            parent[u] = find(parent[u])
            return parent[u]

    def unite(u, v):
        u = find(u)
        v = find(v)
        if u != v:
            parent[u] = v
            return True
        return False

    parent = list(range(2 * n + 1))
    ct = [0, 0]
    both = n - 1
    edges.sort(reverse=True)
    for edge in edges:
        type, u, v = edge
        if type == 3 and unite(u, v + n):
            both -= 1
        if both == 0:
            break

    for type in range(1, 3):
        for edge in edges:
            a, u, v = edge
            if a == type and unite(u, v + n):
                ct[type - 1] += 1
        if both + ct[type - 1] < n - 1:
            return -1

    return ct[0] + ct[1] - n + 1


## Structure
def maxNumEdgesToRemove(n, edges):
    # Your code here

    pass