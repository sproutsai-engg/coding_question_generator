##Question ID: 1418

from collections import defaultdict
from typing import List

def displayTable(orders: List[List[str]]) -> List[List[str]]:
    tables = defaultdict(lambda: defaultdict(int))
    foodSet = set()

    for order in orders:
        tableNumber = int(order[1])
        foodItem = order[2]
        tables[tableNumber][foodItem] += 1
        foodSet.add(foodItem)

    foodList = sorted(foodSet)
    result = [["Table"] + foodList]

    for tableNumber, table in sorted(tables.items()):
        row = [str(tableNumber)]
        row.extend(str(table[foodItem]) for foodItem in foodList)
        result.append(row)

    return result

## Structure
from collections import defaultdict
    # Your code here

    pass