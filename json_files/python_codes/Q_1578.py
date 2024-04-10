##Question ID: 1578

def minTime(colors: str, neededTime: List[int]) -> int:
    res, prev = 0, -1
    for i in range(len(colors) - 1):
        if colors[i] == colors[i + 1]:
            if prev == -1 or neededTime[i] < neededTime[prev]:
                prev = i
            if neededTime[i + 1] < neededTime[prev]:
                prev = i + 1
            res += neededTime[prev]
            neededTime[prev] = 1000000
            prev = -1
    return res

## Structure
def minTime(colors: str, neededTime: List[int]) -> int:
    # Your code here

    pass