##Question ID: 685

def findRedundantDirectedConnection(edges):
    parent = [0] * (len(edges) + 1)
    candidateA = candidateB = None

    for u, v in edges:
        if parent[v] > 0:
            candidateA = [parent[v], v]
            candidateB = [u, v]
        else:
            parent[v] = u

    for i in range(1, len(edges) + 1):
        cycle = i
        steps = len(edges)
        while parent[cycle] != 0 and steps > 0:
            cycle = parent[cycle]
            steps -= 1
        if steps == 0:
            if not candidateA:
                return [parent[i], i]
            else:
                return candidateA

    return candidateB


## Structure
def findRedundantDirectedConnection(edges):
    # Your code here

    pass