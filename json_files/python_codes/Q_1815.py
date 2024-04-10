##Question ID: 1815

from typing import List

def distanceLimitedPathsExist(n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    edgeList.sort(key=lambda x: x[2])
    queries = sorted(enumerate(queries), key=lambda x: x[1][2])

    def find(x: int, parent: List[int]) -> int:
        if x != parent[x]:
            parent[x] = find(parent[x], parent)
        return parent[x]

    parent = list(range(n))
    res = [False] * len(queries)
    idx = 0

    for query_id, query in queries:
        p, q, limit = query
        while idx < len(edgeList) and edgeList[idx][2] < limit:
            u, v = edgeList[idx][:2]
            ru, rv = find(u, parent), find(v, parent)
            if ru != rv:
                parent[ru] = rv
            idx += 1
        res[query_id] = find(p, parent) == find(q, parent)

    return res

## Structure
from typing import List
    # Your code here

    pass