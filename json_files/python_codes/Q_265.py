##Question ID: 265

def min_cost(costs: List[List[int]]) -> int:
    if not costs:
        return 0

    n, k = len(costs), len(costs[0])

    for i in range(1, n):
        for j in range(k):
            min_cost = float("inf")
            for l in range(k):
                if l == j:
                    continue
                min_cost = min(min_cost, costs[i - 1][l])
            costs[i][j] += min_cost

    return min(costs[n - 1])


## Structure
def min_cost(costs: List[List[int]]) -> int:
    # Your code here

    pass