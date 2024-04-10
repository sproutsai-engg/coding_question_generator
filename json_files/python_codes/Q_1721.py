##Question ID: 1721

def min_operations_max_profit(customers, boarding_cost, running_cost):
    rotations = waiting = on_board = profit = max_profit = max_rotations = 0
    while customers or waiting > 0:
        if customers:
            waiting += customers.pop(0)
            
        on_board = min(waiting, 4)
        waiting -= on_board
        profit += on_board * boarding_cost - running_cost
        rotations += 1
        
        if profit > max_profit:
            max_profit = profit
            max_rotations = rotations
            
    return max_rotations if max_profit > 0 else -1


## Structure
def min_operations_max_profit(customers, boarding_cost, running_cost):
    # Your code here

    pass