##Question ID: 1136

def minimum_semesters(n: int, relations: List[List[int]]) -> int:
    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for prev, next in relations:
        graph[prev].append(next)
        in_degree[next] += 1

    q = [i for i in range(1, n + 1) if in_degree[i] == 0]
    semesters = 0

    while q:
        next_q = []
        semesters += 1
        for course in q:
            n -= 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    next_q.append(next_course)
        q = next_q

    return semesters if n == 0 else -1

## Structure
def minimum_semesters(n: int, relations: List[List[int]]) -> int:
    # Your code here

    pass