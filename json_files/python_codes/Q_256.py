##Question ID: 256

def minCost(costs: List[List[int]]) -> int:
    if not costs:
        return 0
    for i in range(1, len(costs)):
        costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
    return min(costs[-1][0], costs[-1][1], costs[-1][2])

## Structure
def minCost(costs: List[List[int]]) -> int:
    # Your code here

    pass