##Question ID: 1066

from typing import List

def manhattan_distance(worker: List[int], bike: List[int]) -> int:
    return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

def dfs(workers: List[List[int]], bikes: List[List[int]], used: List[bool], index: int, dist: int, min_dist: List[int]) -> None:
    if index == len(workers):
        min_dist[0] = min(min_dist[0], dist)
        return

    if dist >= min_dist[0]:
        return

    for i in range(len(bikes)):
        if used[i]:
            continue
        used[i] = True
        cur_dist = manhattan_distance(workers[index], bikes[i])
        dfs(workers, bikes, used, index + 1, dist + cur_dist, min_dist)
        used[i] = False

def assign_bikes(workers: List[List[int]], bikes: List[List[int]]) -> int:
    min_dist = [float('inf')]
    used = [False] * len(bikes)
    dfs(workers, bikes, used, 0, 0, min_dist)
    return min_dist[0]

## Structure
from typing import List
    # Your code here

    pass