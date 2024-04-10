##Question ID: 1774

from itertools import product

def closest_cost(base_costs, topping_costs, target):
    closest = float('inf')
    topping_combinations = list(product([0, 1, 2], repeat=len(topping_costs)))
    
    for base in base_costs:
        for combination in topping_combinations:
            combination_cost = sum(x * y for x, y in zip(topping_costs, combination))
            diff = abs(target - (base + combination_cost))
            if diff < closest:
                closest = diff
            if diff == 0:
                return target

    return target - closest

## Structure
from itertools import product
    # Your code here

    pass