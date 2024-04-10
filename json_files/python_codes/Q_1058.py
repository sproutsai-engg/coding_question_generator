##Question ID: 1058

from math import floor, ceil

def find_rounding_error(prices, target):
    n = len(prices)
    decimals = [float(price) - floor(float(price)) for price in prices]
    rounded_sum = sum(floor(float(price)) for price in prices)

    if target < rounded_sum or target > rounded_sum + n:
        return "-1 "

    ceil_count = target - rounded_sum
    rounding_error = 0.0

    for d in decimals:
        if ceil_count > 0:
            rounding_error += 1 - d
            ceil_count -= 1
        else:
            rounding_error += d

    return f"{rounding_error:.3f} "


## Structure
from math import floor, ceil
    # Your code here

    pass