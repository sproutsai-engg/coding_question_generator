##Question ID: 1595

def connectTwoGroups(cost):
    size1, size2 = len(cost), len(cost[0])
    min_cost = [float('inf')] * size2

    for i in range(size1):
        for j in range(size2):
            min_cost[j] = min(min_cost[j], cost[i][j])

    total_cost = 0
    for i in range(size1):
        total_cost += min(cost[i])

    for j in range(size2):
        total_cost += min_cost[j]

    return total_cost


## Structure
def connectTwoGroups(cost):
    # Your code here

    pass