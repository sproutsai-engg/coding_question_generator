##Question ID: 1599

def minOperationsMaxProfit(customers, boardingCost, runningCost):
    waiting = 0
    profit = 0
    max_profit = 0
    rotations = 0
    result = -1

    for i in range(len(customers) + sum(customers)):
        if i < len(customers):
            waiting += customers[i]
        boarding = min(waiting, 4)
        waiting -= boarding
        profit += boarding * boardingCost - runningCost

        if profit > max_profit:
            max_profit = profit
            result = rotations + 1
        rotations += 1
    
    return result


## Structure
def minOperationsMaxProfit(customers, boardingCost, runningCost):
    # Your code here

    pass