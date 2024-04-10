##Question ID: 1447

def minJumps(arr):
    n = len(arr)
    maxReach = arr[0]
    step = arr[0]
    jumps = 1

    if n == 1:
        return 0

    for i in range(1, n):
        if i == n - 1:
            return jumps

        maxReach = max(maxReach, i + arr[i])

        step -= 1

        if step == 0:
            jumps += 1
            step = maxReach - i

    return -1

## Structure
def minJumps(arr):
    # Your code here

    pass