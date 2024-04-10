##Question ID: 1697

from collections import defaultdict, deque

def distanceLimitedPathsExist(n, edgeList, queries):
    graph = defaultdict(list)

    for u, v, dis in edgeList:
        graph[u].append((v, dis))
        graph[v].append((u, dis))

    answer = [False] * len(queries)
    for i, (pj, qj, limitj) in enumerate(queries):
        q = deque([(pj, 0)])
        visited = [False] * n
        visited[pj] = True

        while q:
            curr_node, curr_dist = q.popleft()

            for next_node, next_dist in graph[curr_node]:
                if curr_dist + next_dist < limitj:
                    if next_node == qj:
                        answer[i] = True
                        break
                    if not visited[next_node]:
                        visited[next_node] = True
                        q.append((next_node, curr_dist + next_dist))
            if answer[i]:
                break

    return answer

## Structure
from collections import defaultdict, deque
    # Your code here

    pass