##Question ID: 1686

def stoneGameVI(aliceValues, bobValues):
    n = len(aliceValues)
    diff = sorted([(aliceValues[i] + bobValues[i], i) for i in range(n)], reverse=True)

    aliceSum, bobSum = 0, 0
    for i in range(n):
        if i % 2 == 0:
            aliceSum += aliceValues[diff[i][1]]
        else:
            bobSum += bobValues[diff[i][1]]
            
    return 0 if aliceSum == bobSum else (1 if aliceSum > bobSum else -1)


## Structure
def stoneGameVI(aliceValues, bobValues):
    # Your code here

    pass