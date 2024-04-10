##Question ID: 121

def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    for price in prices:
        minPrice = min(minPrice, price)
        maxProfit = max(maxProfit, price - minPrice)
    return maxProfit

## Structure
def maxProfit(prices):
    # Your code here

    pass