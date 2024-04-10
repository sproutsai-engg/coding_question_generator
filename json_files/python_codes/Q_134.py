##Question ID: 134

def can_complete_circuit(gas, cost):
    total_gas, total_cost, start, gas_tank = 0, 0, 0, 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        gas_tank += gas[i] - cost[i]
        if gas_tank < 0:
            start = i + 1
            gas_tank = 0
    return -1 if total_gas < total_cost else start

## Structure
def can_complete_circuit(gas, cost):
    # Your code here

    pass