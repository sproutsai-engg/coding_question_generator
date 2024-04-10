##Question ID: 1095

def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0] - x[1])

    totalCost = 0
    n = len(costs) // 2

    for i in range(n):
        totalCost += costs[i][0] + costs[i + n][1]

    return totalCost

## Structure
def twoCitySchedCost(costs):
    # Your code here

    pass