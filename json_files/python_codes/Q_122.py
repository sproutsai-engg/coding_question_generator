##Question ID: 122

def max_profit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

## Structure
def max_profit(prices):
    # Your code here

    pass