##Question ID: 1462

def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    adj_matrix = [[False] * numCourses for _ in range(numCourses)]
    for pre in prerequisites:
        adj_matrix[pre[0]][pre[1]] = True

    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])

    return [adj_matrix[query[0]][query[1]] for query in queries]


## Structure
def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    # Your code here

    pass