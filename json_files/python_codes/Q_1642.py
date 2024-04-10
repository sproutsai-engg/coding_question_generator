##Question ID: 1642

def maxWaterBottles(numBottles: int, numExchange: int) -> int:
    total = numBottles
    while numBottles >= numExchange:
        newBottles = numBottles // numExchange
        total += newBottles
        numBottles = newBottles + numBottles % numExchange
    return total

## Structure
def maxWaterBottles(numBottles: int, numExchange: int) -> int:
    # Your code here

    pass