##Question ID: 1135

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def minimumCost(n, connections):
    connections.sort(key=lambda x: x[2])

    parent = list(range(n + 1))

    cost = 0
    edges = 0
    for c in connections:
        root_x = find(parent, c[0])
        root_y = find(parent, c[1])

        if root_x != root_y:
            parent[root_y] = root_x
            cost += c[2]
            edges += 1

        if edges == n - 1:
            break

    return cost if edges == n - 1 else -1

## Structure
def find(parent, x):
    # Your code here

    pass