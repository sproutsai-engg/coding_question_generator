##Question ID: 1801

from heapq import *

def getNumberOfBacklogOrders(orders):
    buy_orders, sell_orders = [], []
    num_orders, mod = 0, int(1e9) + 7

    for price, amount, order_type in orders:
        if order_type == 0: # buy order
            while amount and sell_orders and sell_orders[0][0] <= price:
                x = min(amount, sell_orders[0][1])
                amount, sell_orders[0][1] = amount - x, sell_orders[0][1] - x
                if sell_orders[0][1] == 0:
                    heappop(sell_orders)
            if amount:
                heappush(buy_orders, (-price, amount))
        else: # sell order
            while amount and buy_orders and -buy_orders[0][0] >= price:
                x = min(amount, buy_orders[0][1])
                amount, buy_orders[0][1] = amount - x, buy_orders[0][1] - x
                if buy_orders[0][1] == 0:
                    heappop(buy_orders)
            if amount:
                heappush(sell_orders, (price, amount))
    
    while buy_orders:
        num_orders = (num_orders + heappop(buy_orders)[1]) % mod

    while sell_orders:
        num_orders = (num_orders + heappop(sell_orders)[1]) % mod

    return num_orders

## Structure
from heapq import *
    # Your code here

    pass