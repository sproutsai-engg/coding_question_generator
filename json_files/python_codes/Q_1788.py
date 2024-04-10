##Question ID: 1788

def stoneGameVI(aliceValues, bobValues):
    n = len(aliceValues)
    sums = sorted([(aliceValues[i] + bobValues[i], i) for i in range(n)], reverse=True)
    
    aliceScore = sum(aliceValues[i] for _, i in sums[::2])
    bobScore = sum(bobValues[i] for _, i in sums[1::2])
    
    return 0 if aliceScore == bobScore else 1 if aliceScore > bobScore else -1

## Structure
def stoneGameVI(aliceValues, bobValues):
    # Your code here

    pass