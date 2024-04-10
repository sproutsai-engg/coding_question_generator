##Question ID: 1928

from heapq import heappush, heappop

def getNumberOfBacklogOrders(orders):
    buy, sell = [], []

    for price, amount, orderType in orders:
        if orderType == 0:
            while amount > 0 and sell and -sell[0][0] <= price:
                executedAmount = min(amount, sell[0][1])
                amount -= executedAmount
                sell[0] = [-sell[0][0], sell[0][1] - executedAmount]
                if sell[0][1] == 0:
                    heappop(sell)
            if amount:
                heappush(buy, [-price, amount])
        else:
            while amount > 0 and buy and buy[0][0] >= price:
                executedAmount = min(amount, buy[0][1])
                amount -= executedAmount
                buy[0] = [buy[0][0], buy[0][1] - executedAmount]
                if buy[0][1] == 0:
                    heappop(buy)
            if amount:
                heappush(sell, [-price, amount])

    res = sum(item[1] for item in buy) + sum(item[1] for item in sell)
    return res % 1000000007


## Structure
from heapq import heappush, heappop
    # Your code here

    pass