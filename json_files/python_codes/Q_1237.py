##Question ID: 1237

def findSolution(customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    results = []
    for x in range(1, 1001):
        for y in range(1, 1001):
            if customfunction.f(x, y) == z:
                results.append([x, y])
            elif customfunction.f(x, y) > z:
                break
    return results

## Structure
def findSolution(customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    # Your code here

    pass