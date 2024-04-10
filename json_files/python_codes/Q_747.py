##Question ID: 747

def minCostClimbingStairs(cost):
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    return min(cost[-1], cost[-2])

## Structure
def minCostClimbingStairs(cost):
    # Your code here

    pass