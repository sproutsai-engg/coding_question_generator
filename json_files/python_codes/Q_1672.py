##Question ID: 1672

def maximumWealth(accounts):
    max_wealth = 0
    for customer in accounts:
        wealth = sum(customer)
        max_wealth = max(max_wealth, wealth)
    return max_wealth

## Structure
def maximumWealth(accounts):
    # Your code here

    pass