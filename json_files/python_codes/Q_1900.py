##Question ID: 1900

def closest_cost(base_costs, topping_costs, target):
    closest = base_costs[0]
    
    for base in base_costs:
        cost = base
        
        for i in range(1 << (len(topping_costs) * 2)):
            bit_mask = i
            
            for j, topping_cost in enumerate(topping_costs):
                cost += (bit_mask & 3) * topping_cost
                bit_mask >>= 2
                
            if abs(target - cost) < abs(target - closest):
                closest = cost
            elif abs(target - cost) == abs(target - closest) and cost < closest:
                closest = cost
                
            cost = base
            
    return closest


## Structure
def closest_cost(base_costs, topping_costs, target):
    # Your code here

    pass