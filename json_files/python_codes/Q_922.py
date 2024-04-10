##Question ID: 922

from collections import defaultdict


def possible_bipartition(n, dislikes):
    def dfs(person, group):
        if person in groups:
            return groups[person] == group
        groups[person] = group
        for other in dislike_list[person]:
            if not dfs(other, -group):
                return False
        return True

    groups = {}
    dislike_list = defaultdict(list)
    for p1, p2 in dislikes:
        dislike_list[p1].append(p2)
        dislike_list[p2].append(p1)

    for person in range(1, n + 1):
        if person not in groups and not dfs(person, 1):
            return False

    return True


## Structure
from collections import defaultdict
    # Your code here

    pass