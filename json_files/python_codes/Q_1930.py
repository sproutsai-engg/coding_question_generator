##Question ID: 1930

def max_consecutive_values(coins):
    coins.sort()
    max_value = 0    
    for coin in coins:
        if coin <= max_value + 1:
            max_value += coin
        else:
            break
    return max_value + 1

## Structure
def max_consecutive_values(coins):
    # Your code here

    pass