##Question ID: 849

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist

## Structure
def maxDistToClosest(seats):
    # Your code here

    pass