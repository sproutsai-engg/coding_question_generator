##Question ID: 1533

from collections import defaultdict
from typing import List

def displayTable(orders: List[List[str]]) -> List[List[str]]:
    foodItems = set()
    tableOrders = defaultdict(lambda: defaultdict(int))

    for order in orders:
        foodItems.add(order[2])
        tableOrders[int(order[1])][order[2]] += 1

    foodItems = sorted(foodItems)
    header = ["Table"] + foodItems
    result = [header]

    for tableNumber, foodOrder in sorted(tableOrders.items()):
        row = [str(tableNumber)] + [str(foodOrder[food]) for food in foodItems]
        result.append(row)

    return result


## Structure
from collections import defaultdict
    # Your code here

    pass