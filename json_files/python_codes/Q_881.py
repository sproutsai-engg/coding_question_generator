##Question ID: 881

from collections import defaultdict

def loudAndRich(richer, quiet):
    n = len(quiet)
    graph = defaultdict(list)
    for r in richer:
        graph[r[1]].append(r[0])

    answer = [-1] * n

    def dfs(x):
        if answer[x] != -1:
            return answer[x]
        answer[x] = x
        for y in graph[x]:
            cand = dfs(y)
            if quiet[cand] < quiet[answer[x]]:
                answer[x] = cand
        return answer[x]

    for i in range(n):
        dfs(i)

    return answer


## Structure
from collections import defaultdict
    # Your code here

    pass