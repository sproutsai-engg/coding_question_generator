##Question ID: 1182

def shortestDistance(colors, queries):
    result = []
    positions = [[] for _ in range(3)]

    for i, color in enumerate(colors):
        positions[color - 1].append(i)

    for query in queries:
        index_positions = positions[query[1] - 1]

        if not index_positions:
            result.append(-1)
        else:
            dist = float('inf')

            for pos in index_positions:
                dist = min(dist, abs(pos - query[0]))

            result.append(dist)

    return result

## Structure
def shortestDistance(colors, queries):
    # Your code here

    pass