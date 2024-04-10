##Question ID: 1518

def numWaterBottles(numBottles: int, numExchange: int) -> int:
    totalBottles = numBottles
    while numBottles >= numExchange:
        newBottles = numBottles // numExchange
        totalBottles += newBottles
        numBottles = newBottles + numBottles % numExchange
    return totalBottles

## Structure
def numWaterBottles(numBottles: int, numExchange: int) -> int:
    # Your code here

    pass