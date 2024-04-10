##Question ID: 599

from typing import List

def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    restaurantMap = {restaurant: i for i, restaurant in enumerate(list1)}

    minSum = float("inf")
    result = []
    for j, restaurant in enumerate(list2):
        if restaurant in restaurantMap:
            totalSum = j + restaurantMap[restaurant]
            if totalSum < minSum:
                result = [restaurant]
                minSum = totalSum
            elif totalSum == minSum:
                result.append(restaurant)

    return result


## Structure
from typing import List
    # Your code here

    pass