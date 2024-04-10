##Question ID: 1872

def can_eat(candiesCount, queries):
    prefix_sum = [0] * (len(candiesCount) + 1)
    for i in range(len(candiesCount)):
        prefix_sum[i + 1] = prefix_sum[i] + candiesCount[i]

    result = [False] * len(queries)
    for i in range(len(queries)):
        favoriteType, favoriteDay, dailyCap = queries[i]
        x1 = favoriteDay + 1
        y1 = (favoriteDay + 1) * dailyCap

        x2 = prefix_sum[favoriteType] + 1
        y2 = prefix_sum[favoriteType + 1]

        result[i] = not (x1 > y2 or y1 < x2)

    return result

## Structure
def can_eat(candiesCount, queries):
    # Your code here

    pass