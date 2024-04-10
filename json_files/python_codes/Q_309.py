##Question ID: 309

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        profit += max(prices[i] - prices[i - 1], 0)
    return profit

## Structure
def maxProfit(prices):
    # Your code here

    pass