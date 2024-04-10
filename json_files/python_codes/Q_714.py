##Question ID: 714

def maxProfit(prices, fee):
    cash, hold = 0, -prices[0]
    for price in prices:
        temp = cash
        cash = max(cash, hold + price - fee)
        hold = max(hold, temp - price)
    return cash

## Structure
def maxProfit(prices, fee):
    # Your code here

    pass