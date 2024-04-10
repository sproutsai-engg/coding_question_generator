##Question ID: 1442

def make_connected(n, connections):
    adj_list = [[] for _ in range(n)]
    visited = [False] * n
    components = 0
    extra_edges = 0

    for a, b in connections:
        adj_list[a].append(b)
        adj_list[b].append(a)

    for i in range(n):
        if not visited[i]:
            components += 1
            stack = [i]

            while stack:
                current = stack.pop()

                if not visited[current]:
                    visited[current] = True

                    for neighbor in adj_list[current]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
                        else:
                            extra_edges += 1

    extra_needed = components - 1

    if extra_edges >= extra_needed:
        return extra_needed

    return -1


## Structure
def make_connected(n, connections):
    # Your code here

    pass