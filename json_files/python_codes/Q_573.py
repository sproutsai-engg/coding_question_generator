##Question ID: 573

def minDistance(height, width, tree, squirrel, nuts):
    totalDist = 0
    minDiff = float("inf")
    
    for nut in nuts:
        treeDist = abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])
        squirrelDist = abs(squirrel[0] - nut[0]) + abs(squirrel[1] - nut[1])
        
        totalDist += 2 * treeDist
        minDiff = min(minDiff, squirrelDist - treeDist)
    
    return totalDist + minDiff


## Structure
def minDistance(height, width, tree, squirrel, nuts):
    # Your code here

    pass