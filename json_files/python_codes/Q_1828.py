##Question ID: 1828

def countPoints(points, queries):
    answer = []
    for query in queries:
        inside = 0
        for point in points:
            dx = point[0] - query[0]
            dy = point[1] - query[1]
            if dx * dx + dy * dy <= query[2] * query[2]:
                inside += 1
        answer.append(inside)
    return answer


## Structure
def countPoints(points, queries):
    # Your code here

    pass