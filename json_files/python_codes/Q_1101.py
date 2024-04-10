##Question ID: 1101

def earliestAcq(logs, n):
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    parents = list(range(n))
    logs.sort()

    group_count = n
    for timestamp, x, y in logs:
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parents[root_x] = root_y
            group_count -= 1
        if group_count == 1:
            return timestamp
    return -1

## Structure
def earliestAcq(logs, n):
    # Your code here

    pass